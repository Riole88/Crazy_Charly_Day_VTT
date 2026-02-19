<?php
namespace application_core\application\usecases;

use application_core\application\usecases\interfaces\AuthServiceInterface;
use infrastructure\repositories\interfaces\UserRepositoryInterface;

class ServiceAuth implements AuthServiceInterface
{
    private AuthServiceInterface $authRepository;
    private UserRepositoryInterface $userRepository;

    public function __construct(AuthServiceInterface $authRepository, UserRepositoryInterface $userRepository)
    {
        $this->authRepository = $authRepository;
        $this->userRepository = $userRepository;
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
        
        // Keycloak returns the new User UUID
        $userId = $this->authRepository->register($email, $password, $firstName, $lastName);

        // Save locally using the same UUID
        $this->userRepository->createUser($userId, $email, $firstName, $lastName, $password);

        return "Utilisateur créé avec succès (ID: $userId)";
    }
}
