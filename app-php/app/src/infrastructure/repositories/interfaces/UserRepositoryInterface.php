<?php
namespace infrastructure\repositories\interfaces;

interface UserRepositoryInterface
{
    public function createUser(string $id, string $email, string $firstName, string $lastName, string $password): void;
    // Add other methods if needed (e.g. findByEmail)
}
