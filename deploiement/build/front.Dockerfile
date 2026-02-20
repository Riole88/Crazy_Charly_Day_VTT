# --- Stage 1: Build Node (Compilation du Front-end) ---
FROM node:20-alpine AS build-stage

# Optionnel : Mise à jour de npm pour éviter les warnings
RUN npm install -g npm@11.10.1

WORKDIR /app

# Copie des fichiers de dépendances
COPY front.charly/package*.json ./

# On installe TOUTES les dépendances (nécessaire pour avoir Vite et les plugins)
RUN npm ci

# Copie du reste du code source
COPY front.charly/ .

# Compilation du projet (Génère le dossier /app/dist)
RUN npm run build

# --- Stage 2: Nginx sécurisé (Service des fichiers statiques) ---
FROM nginx:stable-alpine

# Création d'un dossier pour le cache nginx accessible par l'utilisateur nginx
RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid /var/cache/nginx /var/log/nginx /etc/nginx/conf.d

# On remplace la config par défaut pour écouter sur 8080 (car < 1024 requiert root)
RUN sed -i 's/listen\(.*\)80;/listen 8080;/' /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

# On ne copie QUE les fichiers compilés du stage précédent
# L'option --chown assure que l'utilisateur nginx peut lire les fichiers
COPY --from=build-stage --chown=nginx:nginx /app/dist .

# Sécurité : On utilise l'utilisateur 'nginx' non-root
USER nginx

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]