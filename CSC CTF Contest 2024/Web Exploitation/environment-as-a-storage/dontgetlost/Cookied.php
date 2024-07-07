<?php

if (!isset($_COOKIE['PHPSESSID']) ) 
{
    header('Location: /checkCOOKIE.php');
    exit();
}