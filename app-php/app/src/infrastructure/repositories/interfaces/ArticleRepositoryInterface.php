<?php

namespace infrastructure\repositories\interfaces;

use api\dtos\CreateArticleDTO;
use api\dtos\ModifyArticleDTO;
use application_core\domain\entities\article\Article;

interface ArticleRepositoryInterface {
    public function getArticle(string $id): Article;
    public function getArticles(): array;
    public function createArticle(CreateArticleDTO $createArticleDTO): Article;
    public function modifyArticle(ModifyArticleDTO $modifyArticleDTO): Article;
}