<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscar Partidos</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css" rel="stylesheet">
    <link rel="icon" href="./img/futbolicon.png">
</head>
<body>
    <div class="container mx-auto p-4">
        <div class="flex justify-between">
            <h1 class="text-2xl mb-4">Partidos</h1>
            <a href="./index.php" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">Inicio</a>
        </div>
        <br>
        <div class="flex justify-between">
            <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']) ?>" class="mr-4 p-2 rounded">
            <label for="League">Liga</label>
                <select id="League" class="mr-4 p-2 border border-gray-300 rounded" name="League">
                    <option value="null" selected>-</option>
                    <option value="LaLiga">LaLiga</option>
                    <option value="Premier_League">Premier League</option>
                    <option value="Bundesliga">Bundesliga</option>
                    <option value="Serie_A">Serie A</option>
                    <option value="Ligue_1">Ligue 1</option>
                </select>
                <label for="Season">Temporada</label>
                <select id="Season" class="mr-4 p-2 border border-gray-300 rounded" name="Season">
                    <option value="null" selected>-</option>
                    <option value="2022-2023">2022-2023</option>
                    <option value="2021-2022">2021-2022 </option>
                </select>
                <button type="submit" name="selects" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">Aplicar filtros</button>
            </form>
            <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']) ?>" method="post">
                <div class="flex items-center mr-4">
                    <input type="text" name="equipo" placeholder="Busca un Equipo" class="border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:border-blue-500">
                    <button class="ml-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded" type="submit" name="find">Buscar</button>
                </div>
            </form>
        </div>
        <br>
        <table class="table-auto w-full">
            <thead>
                <tr>
                    <th class="px-4 py-2 bg-gray-200">Fecha</th>
                    <th class="px-4 py-2 bg-gray-200">Temporada</th>
                    <th class="px-4 py-2 bg-gray-200">Equipo Local</th>
                    <th class="px-4 py-2 bg-gray-200">Equipo Visitante</th>
                    <th class="px-4 py-2 bg-gray-200">Goles Equipo Local</th>
                    <th class="px-4 py-2 bg-gray-200">Goles Equipo Visitante</th>
                    <th class="px-4 py-2 bg-gray-200">Resultado</th>
                    <th class="px-4 py-2 bg-gray-200">Liga</th>
                    <th class="px-4 py-2 bg-gray-200">País</th>
                </tr>
            </thead>
            <tbody>
                <?
                    function call_api($url){
                        $json_data = file_get_contents($url);
                        $matches = json_decode($json_data);
                        
                        return $matches;
                    }
                    function fill_table($matches) {
                        foreach ($matches as $match) {
                            echo "
                            <tr>
                                <td class='border bg-white px-4 py-2'>{$match->Date}</td>
                                <td class='border bg-white px-4 py-2'>{$match->Season}</td>
                                <td class='border bg-white px-4 py-2'>{$match->HomeTeam}</td>
                                <td class='border bg-white px-4 py-2'>{$match->AwayTeam}</td>
                                <td class='border bg-white px-4 py-2'>{$match->HomeTeamGoals}</td>
                                <td class='border bg-white px-4 py-2'>{$match->AwayTeamGoals}</td>
                                <td class='border bg-white px-4 py-2'>{$match->Result}</td>
                                <td class='border bg-white px-4 py-2'>{$match->League}</td>
                                <td class='border bg-white px-4 py-2'>{$match->Country}</td>
                            </tr>
                            ";
                        }
                    }
                    if (empty($_POST)) {
                        $api_url = "http://192.168.10.10:5000/matches";
                        $matches = call_api($api_url);

                        fill_table($matches);
                    }
                    elseif (isset($_POST['selects'])) {
                        $league = $_POST['League'];
                        $season = $_POST['Season'];
                        if ($_POST['League'] == "null" and $_POST['Season'] == "null"){
                            $api_url = "http://192.168.10.10:5000/matches";
                            $matches = call_api($api_url);

                            fill_table($matches);
                        }
                        elseif ($_POST['League'] != "null" and $_POST['Season'] == "null"){
                            $api_url = "http://192.168.10.10:5000/matches?league=$league";
                            $matches = call_api($api_url);

                            fill_table($matches);
                        }
                        elseif ($_POST['League'] == "null" and $_POST['Season'] != "null"){
                            $api_url = "http://192.168.10.10:5000/matches?season=$season";
                            $matches = call_api($api_url);

                            fill_table($matches);
                        }
                        else {
                            $api_url = "http://192.168.10.10:5000/matches?league=$league&season=$season";
                            $matches = call_api($api_url);

                            fill_table($matches);
                        }
                    }
                    elseif (isset($_POST['find'])) {
                        $team = $_POST['equipo'];
                        $api_url = "http://192.168.10.10:5000/matches/$team";
                        $matches = call_api($api_url);

                        fill_table($matches);
                    }
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>