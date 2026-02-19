<?php

namespace application_core\application\usecases\interfaces;

use api\dtos\BoxDTO;

interface ServiceBoxInterface {
    public function getBoxByUser(string $id): BoxDTO;
}