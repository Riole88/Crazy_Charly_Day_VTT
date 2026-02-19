<?php
declare(strict_types=1);

use api\actions\ArticlesAction;
use api\actions\SignInAction;
use Slim\App;
use api\actions\ArticleByIdAction;

return function(App $app): App {
    $app->post('/signin', SignInAction::class);

    $app->get('/articles/{id}', ArticleByIdAction::class);
    $app->get('/articles', ArticlesAction::class);

    return $app;
};