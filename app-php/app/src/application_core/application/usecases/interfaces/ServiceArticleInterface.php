<?php

namespace application_core\application\usecases\interfaces;

use api\dtos\ArticleDTO;

interface ServiceArticleInterface {
    public function getArticle(string $id): ArticleDTO;
    public function getArticles(): array;
}