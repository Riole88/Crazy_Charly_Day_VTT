<?php


use api\actions\ArticleByIdAction;
use api\actions\ArticlesAction;
use application_core\application\usecases\interfaces\ServiceArticleInterface;
use Psr\Container\ContainerInterface;

return [
    ArticleByIdAction::class => function (ContainerInterface $c) {
        return new ArticleByIdAction($c->get(ServiceArticleInterface::class));
    },
    ArticlesAction::class => function (ContainerInterface $c) {
        return new ArticlesAction($c->get(ServiceArticleInterface::class));
    },
];

