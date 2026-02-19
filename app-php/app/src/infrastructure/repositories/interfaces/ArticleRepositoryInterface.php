<?php

namespace infrastructure\repositories\interfaces;

use api\dtos\CreateArticleDTO;
use application_core\domain\entities\article\Article;

interface ArticleRepositoryInterface {
    public function getArticle(string $id): Article;
    public function createArticle(CreateArticleDTO $createArticleDTO): Article;
}