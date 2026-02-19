<?php

namespace application_core\application\usecases;

use api\dtos\BoxDTO;
use application_core\application\usecases\interfaces\ServiceBoxInterface;
use infrastructure\repositories\interfaces\BoxRepositoryInterface;

class ServiceBox implements ServiceBoxInterface {
    private BoxRepositoryInterface $boxRepository;

    public function __construct(BoxRepositoryInterface $boxRepository) {
        $this->boxRepository = $boxRepository;
    }

    public function getBoxByUser(string $id): BoxDTO
    {
        try {
            $box = $this->boxRepository->getBoxByUser($id);
        } catch (\Exception $e) {
            throw new \Exception($e->getMessage(), $e->getCode());
        }
        return $this->toDTO($box);
    }

    private function toDTO($box): BoxDTO
    {
        return new BoxDTO(
            id: $box->id,
            name: $box->name,
            totalPrice: $box->totalPrice,
            totalWeight: $box->totalWeight,
            score: $box->score
        );
    }
}