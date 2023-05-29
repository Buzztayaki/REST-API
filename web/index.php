<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Inicio</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css" rel="stylesheet">
</head>
<body style="background-image: url('./img/Fondo4.jpg'); background-size: cover; background-position: center;">
    <div class="min-h-screen flex flex-col justify-center items-center">
        <h1 class="text-4xl text-white">Football Data Page</h1>
        <div class="flex mt-4">
            <a href="./matches.php" class="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded-full mr-2 w-24 h-10">Partidos</a>
            <a href="./classification.php" class="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded-full mr-2">Clasificación</a>
            <a href="./charts.php" class="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded-full">Gráficas</a>
        </div>
    </div>
</body>
</html>