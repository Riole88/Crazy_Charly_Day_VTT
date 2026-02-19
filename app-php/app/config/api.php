<?php


use api\actions\ArticleByIdAction;
use application_core\application\usecases\interfaces\ServiceArticleInterface;
use Psr\Container\ContainerInterface;

return [
    ArticleByIdAction::class => function (ContainerInterface $c) {
        return new ArticleByIdAction($c->get(ServiceArticleInterface::class));
    },
];

