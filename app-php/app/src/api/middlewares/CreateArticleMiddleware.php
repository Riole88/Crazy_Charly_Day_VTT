<?php

namespace api\middlewares;

use api\dtos\CreateArticleDTO;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\RequestHandlerInterface;
use Respect\Validation\Exceptions\NestedValidationException;
use Respect\Validation\Validator as v;
use Slim\Exception\HttpBadRequestException;

class CreateArticleMiddleware {
    public function __invoke(ServerRequestInterface $request, RequestHandlerInterface $next) : ResponseInterface {

        $data = $request->getParsedBody();
        if (!is_array($data)) {
            throw new HttpBadRequestException($request, 'Body JSON invalide.');
        }
        if ($data["price"] < 0.0){
            throw new \Exception("Montant invalide");
        }
        if ($data["weight"] < 0.0){
            throw new \Exception("Poid invalide");
        }

        try {
            v::key('weight', v::numericVal()->notEmpty())
                ->key('price', v::numericVal()->notEmpty())
                ->key('state', v::in(['N', 'TB', 'B']))
                ->key('age', v::in(['BB', 'PE', 'EN', 'AD']))
                ->key('category', v::in(['SOC', 'FIG', 'CON', 'EXT', 'EVL', 'LIV']))
                ->key('designation', v::stringType())
                ->assert($data);

        } catch (NestedValidationException $e) {
            throw new HttpBadRequestException($request, "Invalid data: " . $e->getFullMessage(), $e);
        }

        $articleDTO = new CreateArticleDTO($data["designation"],$data["category"],$data["age"],$data["state"], $data["price"], $data["weight"]);
        $request = $request->withAttribute('article_dto', $articleDTO);

        return $next->handle($request);
    }
}