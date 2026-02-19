FROM quay.io/keycloak/keycloak:latest AS builder

# Configuration pour le build
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true
ENV KC_DB=postgres

WORKDIR /opt/keycloak
# Ici vous pourriez ajouter vos thèmes personnalisés :
# COPY ./themes /opt/keycloak/themes
RUN /opt/keycloak/bin/kc.sh build

# Image finale de prod
FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak/ /opt/keycloak/

# Keycloak tourne par défaut sous l'utilisateur 1000 (keycloak)
USER 1000

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
CMD ["start", "--optimized"]