<?php
namespace infrastructure\repositories;

use application_core\application\usecases\interfaces\AuthServiceInterface;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;
use GuzzleHttp\Exception\RequestException;

class KeycloakAuthRepository implements AuthServiceInterface
{
    private Client $httpClient;
    private array $config;

    public function __construct(array $config)
    {
        $this->httpClient = new Client();
        $this->config = $config;
    }

    public function authenticate(string $email, string $password): string
    {
        $params = [
            'client_id' => $this->config['client_id'],
            'username' => $email,
            'password' => $password,
            'grant_type' => 'password',
        ];

        if (!empty($this->config['client_secret'])) {
            $params['client_secret'] = $this->config['client_secret'];
        }

        try {
            $response = $this->httpClient->post($this->config['auth_url'], [
                'form_params' => $params
            ]);

            $data = json_decode($response->getBody()->getContents(), true);
            return $data['access_token'];

        } catch (GuzzleException $e) {
            $message = $e->getMessage();
            if ($e instanceof RequestException && $e->hasResponse()) {
                $responseBody = $e->getResponse()->getBody()->getContents();
                $message .= " Response: " . $responseBody;
            }
            throw new \Exception("Auth Error: " . $message);
        }
    }

    public function register(string $email, string $password, string $firstName, string $lastName): string
    {
        // 1. Obtenir un token d'admin pour pouvoir créer des users
        // NOTE: Ceci est une méthode "quick & dirty" pour le dév. En prod, utilisez un Service Account dédié.
        try {
            $tokenResponse = $this->httpClient->post('http://keycloak:8080/realms/master/protocol/openid-connect/token', [
                'form_params' => [
                    'client_id' => 'admin-cli',
                    'username' => 'admin', 
                    'password' => 'admin',
                    'grant_type' => 'password',
                ]
            ]);
            $adminToken = json_decode($tokenResponse->getBody()->getContents(), true)['access_token'];
        } catch (GuzzleException $e) {
            throw new \Exception("Erreur interne : Impossible d'obtenir les droits d'administration.");
        }

        // 2. Appel à l'API Admin de Keycloak pour créer l'user
        try {
            $userData = [
                'username' => $email,
                'email' => $email,
                'firstName' => $firstName,
                'lastName' => $lastName,
                'enabled' => true,
                'emailVerified' => true, // Important pour éviter "Account is not fully set up"
                'credentials' => [
                    [
                        'type' => 'password',
                        'value' => $password,
                        'temporary' => false // Important : le mot de passe est définitif
                    ]
                ]
            ];

            $this->httpClient->post('http://keycloak:8080/admin/realms/myrealm/users', [
                'headers' => [
                    'Authorization' => 'Bearer ' . $adminToken,
                    'Content-Type' => 'application/json'
                ],
                'json' => $userData
            ]);
            
            return "Utilisateur créé avec succès";

        } catch (GuzzleException $e) {
            if ($e instanceof RequestException && $e->hasResponse() && $e->getResponse()->getStatusCode() === 409) {
                 throw new \Exception("Un utilisateur avec cet email existe déjà.");
            }
            // Debug failure
            $msg = $e->getMessage();
            if ($e instanceof RequestException && $e->hasResponse()) {
                $msg .= " :: " . $e->getResponse()->getBody()->getContents();
            }
            throw new \Exception("Erreur création utilisateur : " . $msg);
        }
    }
}
