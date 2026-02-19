<?php

use Psr\Container\ContainerInterface;

return [
    // settings
    'displayErrorDetails' => true,
    'logs.dir' => __DIR__ . '/../var/logs',
    'db.config' => __DIR__ . '/.env',

    // Keycloak
    'keycloak.config' => [
        'auth_url' => 'http://keycloak:8080/realms/myrealm/protocol/openid-connect/token',
        'client_id' => 'php-app-client',
        'client_secret' => '', // Client public défini dans realm-config.yaml
    ],

    // infra
     'charly.pdo' => function (ContainerInterface $c) {
        $config = parse_ini_file($c->get('db.config'));
        $dsn = "{$config['charly.driver']}:host={$config['charly.host']};dbname={$config['charly.database']}";
        $user = $config['charly.username'];
        $password = $config['charly.password'];
        return new \PDO($dsn, $user, $password, [\PDO::ATTR_ERRMODE => \PDO::ERRMODE_EXCEPTION]);
    },
];

