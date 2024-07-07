<?php

require 'Cookied.php';

$ban =[
    "cat",
    "/",
    "strings",
    "type",
    "less",
    "head",
    "tail",
    "echo",
    "|",
    "nl",
    "%",
    "'",
    '"',
    "bash",
    "more",
    "@",
    "&",
    "^",
    "*",
    "<",
    ">",
    "\\",
    ";",
    "exec",
    "system",
    "passthru",
    "+",
    " ",
    "cd",
    "ls",
    "find",
    "tree"
];

try
{
    if($_SERVER['REQUEST_METHOD'] ===  'GET')
    {
    
        $kocak = strtolower($_GET['command']);
    
        for($i =0; $i <count($ban); $i++)
        {
            if(str_contains($kocak, $ban[$i]))
            {
    
                header('Location: /' );
                exit();
            }
        }

        $attack = shell_exec($_GET['command']);
        
        if(!isset($attack))
        {
            $attack = "";
        }
        echo "<p>". $attack."</p>";
        echo "<p>note: after submission, should display storedawdaw item</p><br>";        
    }else if($_SERVER['REQUEST_METHOD'] === 'POST')
    {
    
        echo "<h1>Not Found</h1><br><br><p>The requested resource was not found on this server</p>";
    
    }    
}catch(Throwable $e)
{
    echo "Error: " . $e->getMessage() . "<br>";  
    echo "Error code: " . $e->getCode() . "<br>";
}

echo "<br><br><a href=\"/\">Back to item submission</a>";
