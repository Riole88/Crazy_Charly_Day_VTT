<?php

namespace api\dtos;

class BoxDTO {

    public string $id;
    public string $name;
    public float $totalPrice;
    public float $totalWeight;
    public int $score;

    public function __construct(
        string $id,
        string $name,
        float $totalPrice,
        float $totalWeight,
        int $score
    ) {
        $this->id = $id;
        $this->name = $name;
        $this->totalPrice = $totalPrice;
        $this->totalWeight = $totalWeight;
        $this->score = $score;
    }

    public function __get(string $name){
        if(property_exists($this,$name)) {
            return $this->$name;
        }
        throw new \Exception("Propriété '$name' inexistante dans " . __CLASS__);
    }

    public function __set(string $name, $value) {
        if (property_exists($this, $name)) {
            $this->$name = $value;
            return;
        }
        throw new \Exception("Propriété '$name' inexistante dans " . __CLASS__);
    }
}