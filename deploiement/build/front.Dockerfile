# --- Stage 1: Build Node ---
FROM node:20-alpine AS build-stage
WORKDIR /app

# Copie des fichiers de dépendances
COPY front.charly/package*.json ./

# CORRECTION CI-DESSOUS : Suppression du --only=production
# On a besoin des devDependencies pour pouvoir utiliser 'vite'
RUN npm ci

# Copie du code source
COPY front.charly/ .

# Cette commande fonctionnera enfin car Vite sera présent
RUN npm run build

# --- Stage 2: Nginx sécurisé ---
FROM nginx:stable-alpine

# Configuration des droits pour tourner en non-root
RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid /var/cache/nginx /var/log/nginx /etc/nginx/conf.d

# Changement du port par défaut vers 8080
RUN sed -i 's/listen\(.*\)80;/listen 8080;/' /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

# On récupère le build du stage précédent
COPY --from=build-stage --chown=nginx:nginx /app/dist .

USER nginx

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]