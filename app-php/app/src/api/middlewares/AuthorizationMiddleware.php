<?php
namespace api\middlewares;

use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\MiddlewareInterface;
use Psr\Http\Server\RequestHandlerInterface;
use Slim\Psr7\Response;

class AuthorizationMiddleware implements MiddlewareInterface
{
    private string $requiredRole;

    public function __construct(string $requiredRole)
    {
        $this->requiredRole = $requiredRole;
    }

    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        // 1. Récupérer le header Authorization
        $authHeader = $request->getHeaderLine('Authorization');
        if (empty($authHeader) || !preg_match('/Bearer\s+(.*)$/i', $authHeader, $matches)) {
            return $this->errorResponse("Token manquant ou invalide", 401);
        }

        $token = $matches[1];

        // 2. Décoder le token (Sans vérification de signature pour l'instant, juste pour lire les rôles)
        // NOTE: En production, utilisez une librairie comme firebase/php-jwt pour vérifier la signature avec la clé publique de Keycloak !
        $tokenParts = explode('.', $token);
        if (count($tokenParts) !== 3) {
            return $this->errorResponse("Format de token invalide", 401);
        }

        $payload = json_decode(base64_decode(str_replace(['-', '_'], ['+', '/'], $tokenParts[1])), true);

        // 3. Vérifier les rôles dans le claim 'realm_access'
        $roles = $payload['realm_access']['roles'] ?? [];

        if (!in_array($this->requiredRole, $roles)) {
            return $this->errorResponse("Accès interdit : rôle '{$this->requiredRole}' requis", 403);
        }

        // Si tout est bon, on passe à la suite
        return $handler->handle($request);
    }

    private function errorResponse(string $message, int $status): ResponseInterface
    {
        $response = new Response();
        $response->getBody()->write(json_encode(['error' => $message]));
        return $response->withHeader('Content-Type', 'application/json')->withStatus($status);
    }
}
