<?php

use application_core\application\usecases\interfaces\ServiceArticleInterface;
use application_core\application\usecases\ServiceArticle;
use infrastructure\repositories\interfaces\ArticleRepositoryInterface;
use infrastructure\repositories\PDOArticleRepository;
use Psr\Container\ContainerInterface;

return [
    ServiceArticleInterface::class => function (ContainerInterface $c) {
        return new ServiceArticle($c->get(ArticleRepositoryInterface::class));
    },
    ArticleRepositoryInterface::class => function (ContainerInterface $c) {
        return new PDOArticleRepository($c->get("charly.pdo"));
    }
];

