<?php

use api\actions\SignInAction;
use api\actions\SignUpAction;
use application_core\application\usecases\interfaces\ServiceArticleInterface;
use application_core\application\usecases\interfaces\ServiceBoxInterface;
use application_core\application\usecases\ServiceArticle;
use application_core\application\usecases\interfaces\AuthServiceInterface;
use application_core\application\usecases\ServiceAuth;
use application_core\application\usecases\ServiceBox;
use infrastructure\repositories\interfaces\ArticleRepositoryInterface;
use infrastructure\repositories\interfaces\BoxRepositoryInterface;
use infrastructure\repositories\interfaces\UserRepositoryInterface;
use infrastructure\repositories\KeycloakAuthRepository;
use infrastructure\repositories\PDOArticleRepository;
use infrastructure\repositories\PDOBoxRepository;
use infrastructure\repositories\PDOUserRepository;
use Psr\Container\ContainerInterface;

return [
    AuthServiceInterface::class => function (ContainerInterface $c) {
        $repo = new KeycloakAuthRepository($c->get('keycloak.config'));
        $userRepo = $c->get(UserRepositoryInterface::class);
        return new ServiceAuth($repo, $userRepo);
    },

    UserRepositoryInterface::class => function (ContainerInterface $c) {
        return new PDOUserRepository($c->get("charly.pdo"));
    },

    // Ajout explicite de l'Action pour garantir l'injection correcte
    SignInAction::class => function (ContainerInterface $c) {
        return new SignInAction($c->get(AuthServiceInterface::class));
    },

    // Ajout explicite de SignUpAction
    SignUpAction::class => function (ContainerInterface $c) {
        return new SignUpAction($c->get(AuthServiceInterface::class));
    },

    ServiceArticleInterface::class => function (ContainerInterface $c) {
        return new ServiceArticle($c->get(ArticleRepositoryInterface::class));
    },
    ArticleRepositoryInterface::class => function (ContainerInterface $c) {
        return new PDOArticleRepository($c->get("charly.pdo"));
    },
    ServiceBoxInterface::class => function (ContainerInterface $c) {
        return new ServiceBox($c->get(BoxRepositoryInterface::class));
    },
    BoxRepositoryInterface::class => function (ContainerInterface $c) {
        return new PDOBoxRepository($c->get("charly.pdo"));
    }
];

