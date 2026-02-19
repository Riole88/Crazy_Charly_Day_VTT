<?php

namespace infrastructure\repositories;

use api\dtos\CreateArticleDTO;
use api\dtos\ModifyArticleDTO;
use application_core\domain\entities\article\Article;
use application_core\exceptions\EntityNotFoundException;
use infrastructure\repositories\interfaces\ArticleRepositoryInterface;
use PDO;
use Ramsey\Uuid\Uuid;
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

    public function getArticles(): array
    {
        try {
            $stmt = $this->articlePDO->prepare(
                "SELECT id, designation, category, age, state, price, weight FROM article"
            );
            $stmt->execute();
            $articles = [];
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $articles[] = new Article(
                    id: $row['id'],
                    designation: $row['designation'],
                    category: $row['category'],
                    age: $row['age'],
                    state: $row['state'],
                    price: $row['price'],
                    weight: $row['weight']
                );
            }
        } catch(HttpInternalServerErrorException) {
            throw new \Exception("Erreur lors de l'exécution de la requête SQL.", 500);
        } catch(\Throwable $e) {
            throw new \Exception($e->getMessage(), 400);
        }
        return $articles;
    }

    public function createArticle(CreateArticleDTO $createArticleDTO): Article{
        $id = Uuid::uuid4()->toString();
        try {
            $stmt = $this->articlePDO->prepare(
                "INSERT INTO article (id, designation, category, age, state, price, weight) VALUES (:id, :designation, :category, :age, :state, :price, :weight)"
            );
            $stmt->execute([
                'id' => $id,
                'designation' => $createArticleDTO->designation,
                'category' => $createArticleDTO->category,
                'age' => $createArticleDTO->age,
                'state' => $createArticleDTO->state,
                'price' => $createArticleDTO->price,
                'weight' => $createArticleDTO->weight,
            ]);
        } catch (HttpInternalServerErrorException) {
            throw new \Exception("Erreur lors de l'execution de la requete SQL.", 500);
        } catch(\Throwable) {
            throw new \Exception("Erreur lors de l'ajout de la transaction'.", 400);
        }
        return new Article(
            $id,
            $createArticleDTO->designation,
            $createArticleDTO->category,
            $createArticleDTO->age,
            $createArticleDTO->state,
            $createArticleDTO->price,
            $createArticleDTO->weight
        );
    }
    public function modifyArticle(ModifyArticleDTO $modifyArticleDTO): Article{
        try {
            $sql = "
            UPDATE article SET 
                designation = COALESCE(:designation, designation),
                category    = COALESCE(:category, category),
                age         = COALESCE(:age, age),
                state       = COALESCE(:state, state),
                price       = COALESCE(:price, price),
                weight      = COALESCE(:weight, weight)
            WHERE id = :id";

            $stmt = $this->articlePDO->prepare($sql);

            $stmt->execute([
                ':id'          => $modifyArticleDTO->id,
                ':designation' => $modifyArticleDTO->designation,
                ':category'    => $modifyArticleDTO->category,
                ':age'         => $modifyArticleDTO->age,
                ':state'       => $modifyArticleDTO->state,
                ':price'       => $modifyArticleDTO->price,
                ':weight'      => $modifyArticleDTO->weight
            ]);

            $article = $this->getArticle($modifyArticleDTO->id);
        } catch (HttpInternalServerErrorException) {
            throw new \Exception("Erreur lors de l'execution de la requete SQL.", 500);
        } catch(\Throwable) {
            throw new \Exception("Erreur lors de l'ajout de la transaction'.", 400);
        }
        return $article;
    }
}