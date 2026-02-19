<?php
declare(strict_types=1);

use api\actions\ArticlesAction;
use api\actions\SignInAction;
use api\actions\SignUpAction;
use api\actions\BoxByUserAction;
use api\actions\CreateArticleAction;
use api\actions\ModifyArticleAction;
use api\middlewares\AuthorizationMiddleware;
use api\middlewares\CreateArticleMiddleware;
use api\middlewares\ModifyArticleMiddleware;
use Slim\App;
use api\actions\ArticleByIdAction;

return function(App $app): App {
    $app->post('/signin', SignInAction::class);
    $app->post('/signup', SignUpAction::class);

    $app->post("/articles",CreateArticleAction::class)
        ->add(CreateArticleMiddleware::class)
        ->add(new AuthorizationMiddleware('admin')); // Seuls les admins peuvent créer

    $app->patch("/articles/{id}", ModifyArticleAction::class)
        ->add(ModifyArticleMiddleware::class)
        ->add(new AuthorizationMiddleware('admin')); // Seuls les admins peuvent modifier
    $app->get('/users/{id}/boxes', BoxByUserAction::class);
    $app->get("/articles", ArticlesAction::class);
    $app->get("/articles/{id}", ArticleByIdAction::class);

    return $app;
};