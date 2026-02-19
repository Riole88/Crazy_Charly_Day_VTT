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

    /**
     * Inscrit un nouvel utilisateur
     * @param string $email
     * @param string $password
     * @param string $firstName
     * @param string $lastName
     * @return string Message de succès ou ID
     * @throws \Exception
     */
    public function register(string $email, string $password, string $firstName, string $lastName): string;
}
