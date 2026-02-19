FROM quay.io/keycloak/keycloak:latest AS builder
ENV KC_HEALTH_ENABLED=true
ENV KC_DB=postgres
WORKDIR /opt/keycloak
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak/ /opt/keycloak/

# On ajoute le fichier de configuration du Realm
COPY deploiement/realm-export.json /opt/keycloak/data/import/realm.json

# On force l'import au démarrage
ENV KC_IMPORT=/opt/keycloak/data/import/realm.json

USER 1000
ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
CMD ["start", "--optimized", "--import-realm"]