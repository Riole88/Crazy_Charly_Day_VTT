<?php

namespace api\actions;

use application_core\application\usecases\interfaces\ServiceArticleInterface;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

class ArticlesAction {
    private ServiceArticleInterface $serviceArticle;

    public function __construct(ServiceArticleInterface $serviceArticle) {
        $this->serviceArticle = $serviceArticle;
    }

    /**
     * @throws \Exception
     */
    public function __invoke(ServerRequestInterface $request, ResponseInterface $response, array $args): ResponseInterface {
        try {
            $article = $this->serviceArticle->getArticles();
            $response->getBody()->write(json_encode($article));

            return $response->withHeader("Content-Type", "application/json");
        } catch (\Exception $e) {
            throw new \Exception($e->getMessage());
        }
    }
}