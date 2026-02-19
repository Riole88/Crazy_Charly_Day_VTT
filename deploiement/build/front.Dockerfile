# --- Stage 1: Build Node ---
FROM node:20-alpine AS build-stage
WORKDIR /app
COPY front.charly/package*.json ./
RUN npm ci --only=production
COPY front.charly/ .
RUN npm run build

# --- Stage 2: Nginx sécurisé ---
FROM nginx:stable-alpine

# Création d'un dossier pour le cache nginx accessible par l'utilisateur nginx
RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid /var/cache/nginx /var/log/nginx /etc/nginx/conf.d

# On remplace la config par défaut pour écouter sur 8080 (car < 1024 requiert root)
RUN sed -i 's/listen\(.*\)80;/listen 8080;/' /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html
COPY --from=build-stage --chown=nginx:nginx /app/dist .

# Sécurité : On utilise l'utilisateur 'nginx' déjà présent dans l'image alpine
USER nginx

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]