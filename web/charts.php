<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Gráficas de Estadisticas</title>
    <link rel="icon" href="./img/futbolicon.png">
    <style>
      * {
        margin: 0;
        padding: 0;
        font-family: sans-serif;
      }
      .chartMenu {
        width: 100vw;
        height: 40px;
        background: #1A1A1A;
        color: rgba(54, 162, 235, 1);
      }
      .chartMenu p {
        padding: 10px;
        font-size: 20px;
      }
      .chartCard {
        width: 100vw;
        height: calc(100vh - 40px);
        background: rgba(54, 162, 235, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .chartBox {
        width: 700px;
        padding: 20px;
        border-radius: 20px;
        border: solid 3px rgba(54, 162, 235, 1);
        background: white;
      }
    </style>
  </head>
  <body>
    <a href="./index.php">Inicio</a>
    <div class="chartCard">
      <div class="chartBox">
        <canvas id="myChart"></canvas>
        <button onclick="executeRed2122()">Tarjetas Rojas S21-22</button>
        <button onclick="executeRed2223()">Tarjetas Rojas S22-23</button>
        <button onclick="executeaccuracy2122()">Precisión S21-22</button>
        <button onclick="executeaccuracy2223()">Precisión Rojas S22-23</button>
      </div>
    </div>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/chart.js/dist/chart.umd.min.js"></script>
    <script>
    // setup 
    async function redCards2223(){
      const url = 'https://api.cbusseq.com/leaguestats/redcards/2022-2023'
      const response = await fetch(url);
      const datapoints = await response.json();
      return datapoints
    };
    async function redCards2122(){
      const url = 'https://api.cbusseq.com/leaguestats/redcards/2021-2022'
      const response = await fetch(url);
      const datapoints = await response.json();
      return datapoints
    };
    async function accuracy2223(){
      const url = 'https://api.cbusseq.com/leaguestats/accuracy/2022-2023'
      const response = await fetch(url);
      const datapoints = await response.json();
      return datapoints
    };
    async function accuracy2122(){
      const url = 'https://api.cbusseq.com/leaguestats/accuracy/2021-2022'
      const response = await fetch(url);
      const datapoints = await response.json();
      return datapoints
    };
    function executeRed2223() {
      redCards2223().then(datapoints => {
        const leagues = datapoints.map(data => data.League);
        console.log(leagues);
        myChart.config.data.labels = leagues;
        myChart.update();
      });
      redCards2223().then(datapoints => {
        const redcards = datapoints.map(data => data.RedCards);
        myChart.config.data.datasets[0].data = redcards;
        myChart.update();
      });
    }
    function executeRed2122() {
      redCards2122().then(datapoints => {
        const leagues = datapoints.map(data => data.League);
        console.log(leagues);
        myChart.config.data.labels = leagues;
        myChart.update();
      });
      redCards2122().then(datapoints => {
        const redcards = datapoints.map(data => data.RedCards);
        myChart.config.data.datasets[0].data = redcards;
        myChart.update();
      });
    }
    function executeaccuracy2122() {
      accuracy2122().then(datapoints => {
        const leagues = datapoints.map(data => data.League);
        console.log(leagues);
        myChart.config.data.labels = leagues;
        myChart.update();
      });
      accuracy2122().then(datapoints => {
        const accuracy = datapoints.map(data => data.Accuracy);
        myChart.config.data.datasets[0].data = accuracy;
        myChart.update();
      });
    }
    function executeaccuracy2223() {
      accuracy2223().then(datapoints => {
        const leagues = datapoints.map(data => data.League);
        console.log(leagues);
        myChart.config.data.labels = leagues;
        myChart.update();
      });
      accuracy2223().then(datapoints => {
        const accuracy = datapoints.map(data => data.Accuracy);
        myChart.config.data.datasets[0].data = accuracy;
        myChart.update();
      });
    }

    const data = {
      labels: ['', '', '', '', ''],
      datasets: [{
        label: ['', ''],
        data: [0, 0, 0, 0, 0],
        backgroundColor: [
          'rgba(255, 26, 104, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(0, 0, 0, 0.2)'
        ],
        borderColor: [
          'rgba(255, 26, 104, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(0, 0, 0, 1)'
        ],
        borderWidth: 1
      }]
    };

    // config 
    const config = {
      type: 'bar',
      data,
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    };

    // render init block
    const myChart = new Chart(
      document.getElementById('myChart'),
      config
    );

    // Instantly assign Chart.js version
    const chartVersion = document.getElementById('chartVersion');
    chartVersion.innerText = Chart.version;
    </script>
  </body>
</html>