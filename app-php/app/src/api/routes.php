<?php
declare(strict_types=1);

use api\actions\ArticlesAction;
use api\actions\CreateArticleAction;
use api\middlewares\CreateArticleMiddleware;
use Slim\App;
use api\actions\ArticleByIdAction;

return function(App $app): App {
    $app->get('/articles/{id}', ArticleByIdAction::class);
    $app->get('/articles', ArticlesAction::class);
    $app->post("/articles",CreateArticleAction::class)->add(CreateArticleMiddleware::class);;

    return $app;
};