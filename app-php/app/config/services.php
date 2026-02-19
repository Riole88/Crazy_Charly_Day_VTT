<?php

use api\actions\SignInAction;
use application_core\application\usecases\interfaces\ServiceArticleInterface;
use application_core\application\usecases\ServiceArticle;
use application_core\application\usecases\interfaces\AuthServiceInterface;
use application_core\application\usecases\ServiceAuth;
use infrastructure\repositories\interfaces\ArticleRepositoryInterface;
use infrastructure\repositories\KeycloakAuthRepository;
use infrastructure\repositories\PDOArticleRepository;
use Psr\Container\ContainerInterface;

return [
    AuthServiceInterface::class => function (ContainerInterface $c) {
        $repo = new KeycloakAuthRepository($c->get('keycloak.config'));
        return new ServiceAuth($repo);
    },
    
    // Ajout explicite de l'Action pour garantir l'injection correcte
    SignInAction::class => function (ContainerInterface $c) {
        return new SignInAction($c->get(AuthServiceInterface::class));
    },

    ServiceArticleInterface::class => function (ContainerInterface $c) {
        return new ServiceArticle($c->get(ArticleRepositoryInterface::class));
    },
    ArticleRepositoryInterface::class => function (ContainerInterface $c) {
        return new PDOArticleRepository($c->get("charly.pdo"));
    }
];

