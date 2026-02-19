<?php
namespace infrastructure\repositories;

use application_core\application\usecases\interfaces\AuthServiceInterface;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;
use GuzzleHttp\Exception\RequestException;

class KeycloakAuthRepository implements AuthServiceInterface
{
    private Client $httpClient;
    private array $config;

    public function __construct(array $config)
    {
        $this->httpClient = new Client();
        $this->config = $config;
    }

    public function authenticate(string $email, string $password): string
    {
        $params = [
            'client_id' => $this->config['client_id'],
            'username' => $email,
            'password' => $password,
            'grant_type' => 'password',
        ];

        if (!empty($this->config['client_secret'])) {
            $params['client_secret'] = $this->config['client_secret'];
        }

        try {
            $response = $this->httpClient->post($this->config['auth_url'], [
                'form_params' => $params
            ]);

            $data = json_decode($response->getBody()->getContents(), true);
            return $data['access_token'];

        } catch (GuzzleException $e) {
            $message = $e->getMessage();
            if ($e instanceof RequestException && $e->hasResponse()) {
                $responseBody = $e->getResponse()->getBody()->getContents();
                $message .= " Response: " . $responseBody;
            }
            throw new \Exception("Auth Error: " . $message);
        }
    }
}
