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
            <a href="./matches.php" class="relative flex flex-col bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded-lg mr-2 w-40">
                <img src="ruta-a-tu-imagen-1.jpg" alt="Partidos" class="object-cover h-24 rounded-t-lg">
                <span class="mt-auto text-center">Partidos</span>
            </a>
            <a href="./classification.php" class="relative flex flex-col bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded-lg mr-2 w-40">
                <img src="ruta-a-tu-imagen-2.jpg" alt="Clasificación" class="object-cover h-24 rounded-t-lg">
                <span class="mt-auto text-center">Clasificación</span>
            </a>
            <a href="./charts.php" class="relative flex flex-col bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded-lg w-40">
                <img src="ruta-a-tu-imagen-3.jpg" alt="Gráficas" class="object-cover h-24 rounded-t-lg">
                <span class="mt-auto text-center">Gráficas</span>
            </a>
        </div>
    </div>
</body>
</html>