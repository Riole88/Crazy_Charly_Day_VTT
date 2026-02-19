<?php
session_start();

$realm = "myrealm";
$clientId = "php-app-client";
// Note: On utilise 'localhost' pour les liens cliqués par l'utilisateur (navigateur)
// Et 'keycloak' (nom du container) pour les appels cURL internes.
$keycloakExternalUrl = "http://localhost:8080/realms/$realm/protocol/openid-connect";
$redirectUri = "http://localhost:8000/index.php";

// 1. Échange du code contre un Token
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
    header("Location: $redirectUri");
    exit;
}

// 2. Page d'accueil (Connecté)
if (isset($_SESSION['token']['access_token'])) {
    $payload = json_decode(base64_decode(explode('.', $_SESSION['token']['access_token'])[1]), true);
    echo "<h1>Bienvenue, " . htmlspecialchars($payload['preferred_username']) . " !</h1>";
    echo "<p>Identifiant Keycloak : " . $payload['sub'] . "</p>";
    echo "<p>Email : " . ($payload['email'] ?? 'Non renseigné') . "</p>";
    echo "<a href='?logout=1'>Se déconnecter</a>";
    
    if (isset($_GET['logout'])) {
        session_destroy();
        header("Location: $redirectUri");
    }
    exit;
}

// 3. Page de connexion (Non connecté)
$authUrl = "$keycloakExternalUrl/auth?" . http_build_query([
    'client_id' => $clientId,
    'redirect_uri' => $redirectUri,
    'response_type' => 'code',
    'scope' => 'openid email profile'
]);

echo "<h1>Mon App PHP (Keycloak Natif)</h1>";
echo "<p>L'inscription est activée sur l'écran de connexion.</p>";
echo "<a href='$authUrl' style='padding:10px; background:green; color:white; text-decoration:none; border-radius:5px;'>Se connecter ou S'inscrire</a>";
