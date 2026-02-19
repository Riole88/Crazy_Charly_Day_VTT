<?php

use Psr\Container\ContainerInterface;

return [
    'displayErrorDetails' => true,
    'logs.dir' => __DIR__ . '/../var/logs',
    // Plus besoin de db.config pointant vers un fichier .ini

    'keycloak.config' => [
        'auth_url' => getenv('KC_URL') . '/realms/myrealm/protocol/openid-connect/token',
        'client_id' => 'php-app-client',
        'client_secret' => '',
    ],

    'charly.pdo' => function (ContainerInterface $c) {
        // On récupère directement les infos du système (injectées par Docker)
        $driver   = getenv('CHARLY_DB_DRIVER') ?: 'pgsql';
        $host     = getenv('CHARLY_DB_HOST');
        $dbname   = getenv('CHARLY_DB_NAME');
        $user     = getenv('CHARLY_DB_USER');
        $password = getenv('CHARLY_DB_PASS');

        $dsn = "{$driver}:host={$host};dbname={$dbname}";
        
        return new \PDO($dsn, $user, $password, [
            \PDO::ATTR_ERRMODE => \PDO::ERRMODE_EXCEPTION
        ]);
    },
];