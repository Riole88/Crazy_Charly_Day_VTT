<?php

namespace application_core\application\usecases;



use api\dtos\ArticleDTO;
use application_core\application\usecases\interfaces\ServiceArticleInterface;
use EntityNotFoundException;
use infrastructure\repositories\interfaces\ArticleRepositoryInterface;

class ServiceArticle implements ServiceArticleInterface {
    private ArticleRepositoryInterface $articleRepository;

    public function __construct(ArticleRepositoryInterface $articleRepository) {
        $this->articleRepository = $articleRepository;
    }

    public function getArticle(string $id): ArticleDTO
    {
        try{
            $article = $this->articleRepository->getArticle($id);
        } catch (EntityNotFoundException $e) {
            throw new EntityNotFoundException($e->getEntity()." non trouvé", $e->getEntity());
        } catch (\Exception $e) {
            throw new \Exception($e->getMessage(), $e->getCode());
        }
        return $this->toDTO($article);
    }

    public function getArticles(): array
    {
        try {
            $articles = $this->articleRepository->getArticles();
        } catch (\Exception $e) {
            throw new \Exception($e->getMessage(), $e->getCode());
        }
        return array_map(fn ($art) => $this->toDTO($art), $articles);
    }


    private function toDTO($article): ArticleDTO
    {
        return new ArticleDTO(
            id: $article->id,
            designation: $article->designation,
            category: $article->category,
            age: $article->age,
            state: $article->state,
            price: $article->price,
            weight: $article->weight,
        );
    }
}