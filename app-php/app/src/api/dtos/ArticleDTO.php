<?php

namespace api\dtos;

class ArticleDTO{

    public string $id;
    public string $designation;
    public string $category;
    public string $age;
    public string $state;
    public float $price;
    public float $weight;

    public function __construct(
        string $id,
        string $designation,
        string $category,
        string $age,
        string $state,
        float $price,
        float $weight
    ) {
        $this->weight = $weight;
        $this->price = $price;
        $this->state = $state;
        $this->age = $age;
        $this->category = $category;
        $this->designation = $designation;
        $this->id = $id;
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