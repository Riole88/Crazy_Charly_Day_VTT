<?php
namespace application_core\application\usecases\interfaces;

interface AuthServiceInterface
{
    /**
     * Authentifie un utilisateur et retourne un token
     * @param string $email
     * @param string $password
     * @return string Le token d'accès
     * @throws \Exception
     */
    public function authenticate(string $email, string $password): string;
}
