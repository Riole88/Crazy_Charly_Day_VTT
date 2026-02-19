<?php
session_start();

$realm = "myrealm";
$clientId = "php-app-client";
$keycloakBaseUrl = "http://localhost:8080/realms/$realm/protocol/openid-connect";
$redirectUri = "http://localhost:8000/index.php";

// 1. Si on reçoit un 'code' de Keycloak, on l'échange contre un Token
if (isset($_GET['code'])) {
    $tokenUrl = "http://keycloak:8080/realms/$realm/protocol/openid-connect/token";
    
    $ch = curl_init($tokenUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
        'grant_type' => 'authorization_code',
        'client_id' => $clientId,
        'code' => $_GET['code'],
        'redirect_uri' => $redirectUri,
    ]));

    $response = curl_exec($ch);
    $_SESSION['token'] = json_decode($response, true);
    header("Location: $redirectUri"); // On nettoie l'URL
    exit;
}

// 2. Si on est connecté, on affiche les infos
if (isset($_SESSION['token']['access_token'])) {
    $payload = json_decode(base64_decode(explode('.', $_SESSION['token']['access_token'])[1]), true);
    echo "<h1>Bienvenue, " . htmlspecialchars($payload['preferred_username']) . " !</h1>";
    echo "<p>Tu es connecté via Keycloak et LLDAP.</p>";
    echo "<a href='?logout=1'>Se déconnecter</a>";
    
    if (isset($_GET['logout'])) {
        session_destroy();
        header("Location: $redirectUri");
    }
    exit;
}

// 3. Sinon, on affiche le bouton de connexion
$authUrl = "$keycloakBaseUrl/auth?" . http_build_query([
    'client_id' => $clientId,
    'redirect_uri' => $redirectUri,
    'response_type' => 'code',
    'scope' => 'openid'
]);

echo "<h1>Mon App PHP Sécurisée</h1>";
echo "<a href='$authUrl' style='padding:10px; background:blue; color:white; text-decoration:none;'>Se connecter avec Keycloak</a>";
