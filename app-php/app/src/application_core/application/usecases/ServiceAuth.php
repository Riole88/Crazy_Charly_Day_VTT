<?php
namespace application_core\application\usecases;

use application_core\application\usecases\interfaces\AuthServiceInterface;

class ServiceAuth implements AuthServiceInterface
{
    private AuthServiceInterface $authRepository;

    public function __construct(AuthServiceInterface $authRepository)
    {
        $this->authRepository = $authRepository;
    }

    public function authenticate(string $email, string $password): string
    {
        if (empty($email) || empty($password)) {
            throw new \Exception("Email et mot de passe requis.");
        }
        
        return $this->authRepository->authenticate($email, $password);
    }

    public function register(string $email, string $password, string $firstName, string $lastName): string
    {
        if (empty($email) || empty($password)) {
            throw new \Exception("Email et mot de passe requis.");
        }
        if (empty($firstName) || empty($lastName)) {
            throw new \Exception("Prénom et nom requis.");
        }
        if (strlen($password) < 4) { // Pour l'exemple, Keycloak a ses propres règles
             throw new \Exception("Le mot de passe est trop court.");
        }
        
        return $this->authRepository->register($email, $password, $firstName, $lastName);
    }
}
