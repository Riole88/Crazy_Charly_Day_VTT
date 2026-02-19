<?php

namespace infrastructure\repositories\interfaces;

use application_core\domain\entities\article\Article;

interface ArticleRepositoryInterface {
    public function getArticle(string $id): Article;
    public function getArticles(): array;
}