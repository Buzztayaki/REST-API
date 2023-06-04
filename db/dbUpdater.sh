#!/bin/bash

data="/home/carlos/db/matchesdata2021-2023.csv"
data2="/home/carlos/db/matchesdata.csv"
PyScript="/home/carlos/db/datascraper.py"
logFile="/home/carlos/db/mongoimports.log"
date=$(date +"%Y/%m/%d %H:%M:%S")

echo "[$date] Comienza el update de la base de datos" >> $logFile

if [ -f $data ] || [ -f $data2 ]; then
        rm $data $data2
        echo "Archivo $data antiguo eliminado" >> $logFile
else
        echo "No se encontro archivo $data anterior" >> $logFile
fi


if [ ! -f $PyScript ]; then
        echo "No se encontro el archivo $PyScript terminando el programa" >> $logFile
        exit 1
else
        echo "Se empieza a ejecutar $PyScript" >> $logFile
        python3 $PyScript > /dev/null 2>&1
        sleep 5
fi


if [ ! -f $data ]; then
        echo "No se ha generado el archivo $data terminando el programa" >> $logFile
else
        echo "Archivo $data generado y Headerline borrado"
        sed -i '1d' "$data" #Elimina el Headerline
	cut -d ',' -f 2- matchesdata2021-2023.csv > matchesdata.csv
        mongoimport --uri 'mongodb://carlos:carlos@localhost:27017/football?authSource=admin' --collection matches --drop --type csv --ignoreBlanks --columnsHaveTypes --fieldFile=fields.txt --file matchesdata.csv
        rm $data $data2
	echo "Base de datos actualizada"
fi