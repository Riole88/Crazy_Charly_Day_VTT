<?php

namespace application_core\application\usecases\interfaces;

use api\dtos\ArticleDTO;
use api\dtos\CreateArticleDTO;
use api\dtos\ModifyArticleDTO;

interface ServiceArticleInterface {
    public function getArticle(string $id): ArticleDTO;
    public function getArticles(): array;
    public function createArticle(CreateArticleDTO $createArticleDTO): ArticleDTO;
    public function modifyArticle(ModifyArticleDTO $modifyArticleDTO): ArticleDTO;
}