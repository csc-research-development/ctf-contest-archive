<!DOCTYPE html>
<html lang="en" class="h-full bg-gray-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EnvironmentAsAService</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="h-full">

<div class="min-h-full">

<?php require "partials/head.php"?>
  <main>
    
    <div class="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
      <form action="/Inject.php" method="post" autocomplete="off">
        <label for="command"></label>
        <input type=text name="command" value=""><br>
        <input type="submit" value="Store">
      </form>
    </div>

  </main>
</div>

</body>
</html>