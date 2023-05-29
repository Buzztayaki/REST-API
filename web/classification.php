<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla de Clasificación</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-4">
        <div class="flex justify-between">
            <h1 class="text-2xl mb-4">Clasificación</h1>
            <a href="./index.php" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">Inicio</a>
        </div>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']) ?>" class="mr-4 p-2 rounded">
        <label for="League">Liga</label>
            <select id="League" class="mr-4 p-2 border border-gray-300 rounded" name="League">
                <option value="LaLiga" selected>LaLiga</option>
                <option value="Premier_League">Premier League</option>
                <option value="Bundesliga">Bundesliga</option>
                <option value="Serie_A">Serie A</option>
                <option value="Ligue_1">Ligue 1</option>
            </select>
            <label for="Season">Temporada</label>
            <select id="Season" class="mr-4 p-2 border border-gray-300 rounded" name="Season">
                <option value="2022-2023" selected>2022-2023</option>
                <option value="2021-2022">2021-2022 </option>
            </select>
            <button type="submit" name="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">Aplicar filtros</button>
        </form>
        <table class="table-auto w-full">
            <thead>
                <tr>
                    <th class="px-4 py-2 bg-gray-200">Equipo</th>
                    <th class="px-4 py-2 bg-gray-200">Partidos Jugados</th>
                    <th class="px-4 py-2 bg-gray-200">Victorias</th>
                    <th class="px-4 py-2 bg-gray-200">Empates</th>
                    <th class="px-4 py-2 bg-gray-200">Derrotas</th>
                    <th class="px-4 py-2 bg-gray-200">Goles a Favor</th>
                    <th class="px-4 py-2 bg-gray-200">Goles en Contra</th>
                    <th class="px-4 py-2 bg-gray-200">Diferencia de Goles</th>
                    <th class="px-4 py-2 bg-gray-200">Puntos</th>
                </tr>
            </thead>
            <tbody>
                <?php
                    if (empty($_POST)) {
                        $league = "LaLiga";
                        $season = "2022-2023";
                    }
                    else {
                        $league = $_POST['League'];
                        $season = $_POST['Season'];
                    }
                    // Obtener los datos de la API
                    $api_url = "http://localhost:5000/classification/$league?season=$season";
                    $json_data = file_get_contents($api_url);
                    $equipos = json_decode($json_data);

                    // Recorrer los usuarios y mostrarlos en la tabla
                    foreach ($equipos as $equipo) {
                        echo "
                        <tr>
                            <td class='border bg-white px-4 py-2'>{$equipo->_id}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->MatchesPlayed}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->Wins}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->Draws}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->Losses}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->GoalsFor}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->GoalsAgainst}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->GoalDifference}</td>
                            <td class='border bg-white px-4 py-2'>{$equipo->Points}</td>
                        </tr>
                        ";
                    }
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>