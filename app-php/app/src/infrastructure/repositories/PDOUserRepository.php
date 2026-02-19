<?php
namespace infrastructure\repositories;

use infrastructure\repositories\interfaces\UserRepositoryInterface;
use PDO;

class PDOUserRepository implements UserRepositoryInterface
{
    private PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function createUser(string $id, string $email, string $firstName, string $lastName, string $password): void
    {
        $stmt = $this->pdo->prepare("INSERT INTO users (id, email, first_name, last_name, password, role) VALUES (:id, :email, :first_name, :last_name, :password, 'user')");
        $stmt->execute([
            'id' => $id,
            'email' => $email,
            'first_name' => $firstName,
            'last_name' => $lastName,
            'password' => password_hash($password, PASSWORD_DEFAULT)
        ]);
    }
}
