<?php

namespace api\middlewares;

use api\dtos\ModifyArticleDTO;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\RequestHandlerInterface;
use Respect\Validation\Exceptions\NestedValidationException;
use Respect\Validation\Validator as v;
use Slim\Exception\HttpBadRequestException;
use Slim\Routing\RouteContext;

class ModifyArticleMiddleware {
    public function __invoke(ServerRequestInterface $request, RequestHandlerInterface $next) : ResponseInterface {

        $data = $request->getParsedBody();
        if (!is_array($data)) {
            throw new HttpBadRequestException($request, 'Body JSON invalide.');
        }

        $routeContext = RouteContext::fromRequest($request);
        $route = $routeContext->getRoute();
        $id = $route->getArgument('id');

        try {
            v::key('weight', v::optional(v::numericVal()->positive()), false)
                ->key('price', v::optional(v::numericVal()->positive()), false)
                ->key('state', v::optional(v::in(['N', 'TB', 'B'])), false)
                ->key('age', v::optional(v::in(['BB', 'PE', 'EN', 'AD'])), false)
                ->key('category', v::optional(v::in(['SOC', 'FIG', 'CON', 'EXT', 'EVL', 'LIV'])), false)
                ->key('designation', v::optional(v::stringType()), false)
                ->assert($data);

        } catch (NestedValidationException $e) {
            throw new HttpBadRequestException($request, "Invalid data: " . $e->getFullMessage(), $e);
        }

        $articleDTO = new ModifyArticleDTO(
            $id,
            $data["designation"] ?? null,
            $data["category"]?? null,
            $data["age"]?? null,
            $data["state"]?? null,
            $data["price"]?? null,
            $data["weight"]?? null
        );
        $request = $request->withAttribute('modify_article_dto', $articleDTO);

        return $next->handle($request);
    }
}