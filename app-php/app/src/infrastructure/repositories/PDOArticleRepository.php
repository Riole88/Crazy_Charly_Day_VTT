<?php

namespace infrastructure\repositories;

use application_core\domain\entities\article\Article;
use EntityNotFoundException;
use infrastructure\repositories\interfaces\ArticleRepositoryInterface;
use PDO;
use Slim\Exception\HttpInternalServerErrorException;

class PDOArticleRepository implements ArticleRepositoryInterface {

    private PDO $articlePDO;

    public function __construct(PDO $articlePDO) {
        $this->articlePDO = $articlePDO;
    }

    public function getArticle(string $id): Article
    {
        try {
            $stmt = $this->articlePDO->prepare(
                "SELECT id, designation, category, age, state, price, weight FROM article WHERE id = :id"
            );

            $stmt->execute(
                ['id' => $id]
            );
            $array = $stmt->fetch(PDO::FETCH_ASSOC);

            if (!$array) {
                throw new EntityNotFoundException("Aucun article trouvé.", "article");
            }
            return new Article(
                id: $array['id'],
                designation: $array['designation'],
                category: $array['category'],
                age: $array['age'],
                state: $array['state'],
                price: $array['price'],
                weight: $array['weight']
            );

        } catch (EntityNotFoundException $e) {
            throw $e;
        } catch(HttpInternalServerErrorException) {
            throw new \Exception("Erreur lors de l'exécution de la requête SQL.", 500);
        } catch(\Throwable $e) {
            throw new \Exception($e->getMessage(), 400);
        }
    }
}