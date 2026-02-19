<?php

namespace api\actions;

use application_core\application\usecases\interfaces\ServiceArticleInterface;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Slim\Exception\HttpBadRequestException;

class CreateArticleAction
{
    private ServiceArticleInterface $serviceArticle;

    public function __construct(ServiceArticleInterface $serviceArticle)
    {
        $this->serviceArticle = $serviceArticle;
    }

    public function __invoke(ServerRequestInterface $request, ResponseInterface $response, array $args): ResponseInterface
    {
        $article_dto = $request->getAttribute('article_dto') ?? null;

        if(is_null($article_dto)) {
            throw new \Exception("Erreur récupération DTO de création d'un article");
        }

        try {
            $article = $this->serviceArticle->createArticle($article_dto);
        } catch (\InvalidArgumentException $e) {
            throw new HttpBadRequestException($request, $e->getMessage());
        } catch (\Exception $e) {
            throw new HttpBadRequestException($request, 'Erreur: ' . $e->getMessage());
        }

        $response->getBody()->write(json_encode($article));
        return $response
            ->withHeader('Content-Type', 'application/json')
            ->withStatus(201);
    }
}
