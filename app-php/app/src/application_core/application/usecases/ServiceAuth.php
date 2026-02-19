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
}
