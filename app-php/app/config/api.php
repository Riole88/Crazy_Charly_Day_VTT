<?php


use api\actions\ArticleByIdAction;
use api\actions\CreateArticleAction;
use application_core\application\usecases\interfaces\ServiceArticleInterface;
use Psr\Container\ContainerInterface;

return [
    ArticleByIdAction::class => function (ContainerInterface $c) {
        return new ArticleByIdAction($c->get(ServiceArticleInterface::class));
    },
    CreateArticleAction::class => function (ContainerInterface $c) {
        return new CreateArticleAction($c->get(ServiceArticleInterface::class));
    },
];

