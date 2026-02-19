<?php

namespace infrastructure\repositories;


use application_core\domain\entities\box\Box;
use application_core\exceptions\EntityNotFoundException;
use infrastructure\repositories\interfaces\BoxRepositoryInterface;
use PDO;
use Slim\Exception\HttpInternalServerErrorException;

class PDOBoxRepository implements BoxRepositoryInterface {

    private PDO $boxPDO;

    public function __construct(PDO $boxPDO) {
        $this->boxPDO = $boxPDO;
    }


    public function getBoxByUser(string $id): Box
    {
        try {
            $stmt = $this->boxPDO->prepare(
                "SELECT box.id, box.name, box.total_price, box.total_weight, box.score FROM box INNER JOIN user2box ON box.id = user2box.id_box WHERE user2box.id_user = :id"
            );

            $stmt->execute(
                ['id' => $id]
            );
            $array = $stmt->fetch(PDO::FETCH_ASSOC);

            if (!$array) {
                throw new EntityNotFoundException("Aucune box trouvée.", "box");
            }
            return new Box(
                id: $array['id'],
                name: $array['name'],
                totalPrice: $array['total_price'],
                totalWeight: $array['total_weight'],
                score: $array['score']
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