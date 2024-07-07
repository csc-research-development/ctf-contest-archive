<?php

if(isset(parse_url($_SERVER["REQUEST_URI"])['path']))
{
    $uri = parse_url($_SERVER["REQUEST_URI"])['path'];
}

if(isset(parse_url($_SERVER["REQUEST_URI"])['query']))
{
    $query = parse_url($_SERVER["REQUEST_URI"])['query'];
}

$routes = 
[
    '/' => 'Controller/index.php',
    '/checkCOOKIE.php' => 'Controller/toRegis.php'
];

if(array_key_exists($uri,$routes))
{
    require $routes[$uri];
}
else
{
    require $routes['/'];
}
