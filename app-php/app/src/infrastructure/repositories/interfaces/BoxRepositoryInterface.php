<?php

namespace infrastructure\repositories\interfaces;

use application_core\domain\entities\box\Box;

interface BoxRepositoryInterface {
    public function getBoxByUser(string $id): Box;
}