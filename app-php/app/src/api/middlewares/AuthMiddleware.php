<?php
namespace api\middlewares;

use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\RequestHandlerInterface;
use Slim\Psr7\Response;
use GuzzleHttp\Client;

class AuthMiddleware
{
    private Client $httpClient;
    // Idéalement injecté via config
    private string $introspectionUrl = 'http://keycloak:8080/realms/master/protocol/openid-connect/token/introspect';
    private string $clientId = 'php-api';
    private string $clientSecret = 'votre-secret';

    public function __construct() {
        $this->httpClient = new Client();
    }

    public function __invoke(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        $authHeader = $request->getHeaderLine('Authorization');
        if (!$authHeader || !preg_match('/Bearer\s+(.*)$/i', $authHeader, $matches)) {
            $response = new Response();
            $response->getBody()->write(json_encode(['error' => 'Token manquant']));
            return $response->withStatus(401)->withHeader('Content-Type', 'application/json');
        }

        $token = $matches[1];

        try {
            // Vérification auprès de Keycloak
            $res = $this->httpClient->post($this->introspectionUrl, [
                'form_params' => [
                    'token' => $token,
                    'client_id' => $this->clientId,
                    'client_secret' => $this->clientSecret
                ]
            ]);
            
            $data = json_decode($res->getBody(), true);
            
            if (($data['active'] ?? false) !== true) {
                throw new \Exception("Token invalide ou expiré");
            }

            // On peut injecter les infos user dans la requête pour les actions suivantes
            $request = $request->withAttribute('user_id', $data['sub'] ?? null);

        } catch (\Exception $e) {
            $response = new Response();
            $response->getBody()->write(json_encode(['error' => 'Non autorisé: ' . $e->getMessage()]));
            return $response->withStatus(401)->withHeader('Content-Type', 'application/json');
        }

        return $handler->handle($request);
    }
}