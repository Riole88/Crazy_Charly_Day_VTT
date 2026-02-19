<?php
declare(strict_types=1);

use Slim\App;
use api\actions\ArticleByIdAction;

return function(App $app): App {
    $app->get('/articles/{id}', ArticleByIdAction::class);

    return $app;
};