<?php
// src/Controller/CalcController.php
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\JsonResponse;

class CalcController
{
    public function add($num1, $num2): Response
    {
        return new JsonResponse(['result' => $num1 + $num2]);
    }

    public function substract($num1, $num2): Response
    {
        return new JsonResponse(['result' => $num1 - $num2]);
    }

    public function multiply($num1, $num2): Response
    {
        return new JsonResponse(['result' => $num1 * $num2]);
    }

    public function divide($num1, $num2): Response
    {
        return new JsonResponse(['result' => $num1 / $num2]);
    }
}