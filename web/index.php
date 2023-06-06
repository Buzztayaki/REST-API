<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css" rel="stylesheet">
    <link rel="icon" href="./img/futbolicon.png">
</head>
<body style="background-image: url('./img/fondo10.jpeg'); background-size: cover; background-position: center;">
    <div class="min-h-screen flex flex-col justify-center items-center">
        <h1 class="text-4xl text-white">Football Data Page</h1>
        <div class="flex mt-4">
            <a href="./matches.php" class="relative flex flex-col bg-white bg-opacity-50 hover:bg-opacity-75 text-white font-semibold py-2 px-4 rounded-lg mr-2 w-40">
                <img src="./img/matches.jpg" alt="Partidos" class="object-cover h-24 rounded-t-lg">
                <span class="mt-auto text-center">Partidos</span>
            </a>
            <a href="./classification.php" class="relative flex flex-col bg-white bg-opacity-50 hover:bg-opacity-75 text-white font-semibold py-2 px-4 rounded-lg mr-2 w-40">
                <img src="./img/cup.jpg" alt="Clasificación" class="object-cover h-24 rounded-t-lg">
                <span class="mt-auto text-center">Clasificación</span>
            </a>
            <a href="./charts.php" class="relative flex flex-col bg-white bg-opacity-50 hover:bg-opacity-75 text-white font-semibold py-2 px-4 rounded-lg w-40">
                <img src="./img/graficas.png" alt="Gráficas" class="object-cover h-24 rounded-t-lg">
                <span class="mt-auto text-center">Gráficas</span>
            </a>
        </div>
    </div>
</body>
</html>