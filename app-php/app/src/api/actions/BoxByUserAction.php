<?php

namespace api\actions;

use application_core\application\usecases\interfaces\ServiceBoxInterface;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

class BoxByUserAction {
    private ServiceBoxInterface $serviceBox;

    public function __construct(ServiceBoxInterface $serviceBox) {
        $this->serviceBox = $serviceBox;
    }

    /**
     * @throws \Exception
     */
    public function __invoke(ServerRequestInterface $request, ResponseInterface $response, array $args): ResponseInterface {
        $id = $args['id'] ?? null;
        if(empty($id)) {
            throw new \Exception("Saisissez un id d'utilisateur");
        }

        try {
            $article = $this->serviceBox->getBoxByUser($id);
            $response->getBody()->write(json_encode($article));

            return $response->withHeader("Content-Type", "application/json");
        } catch (\Exception $e) {
            throw new \Exception($e->getMessage());
        }
    }
}