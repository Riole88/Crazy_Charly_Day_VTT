# --- Stage 1: Build (Composer) ---
FROM composer:2 AS vendor
WORKDIR /app
COPY app-php/app/composer.json app-php/app/composer.lock ./
RUN composer install --no-dev --optimize-autoloader --no-interaction

# --- Stage 2: Runtime ---
FROM php:8.4-cli-alpine

# Installation sécurisée des extensions
RUN curl -sSLf -o /usr/local/bin/install-php-extensions \
    https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions && \
    chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions opcache intl zip pdo_pgsql pdo_mysql

# Config de production
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

# Création d'un utilisateur non-root sécurisé
# -D : pas de mot de passe, -S : utilisateur système
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /var/php

# On copie le code avec les bonnes permissions directement
COPY --from=vendor --chown=appuser:appgroup /app/vendor ./vendor
COPY --chown=appuser:appgroup ./app-php/app .

# On bascule sur l'utilisateur restreint
USER appuser

EXPOSE 80
CMD ["php", "-S", "0.0.0.0:80", "-t", "public"]