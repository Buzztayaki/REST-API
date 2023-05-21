#!/bin/bash

data="/home/carlos/matchesdata2022-2023.csv"
PyScript="/home/carlos/datascrambler.py"
logFile="/home/carlos/mongoimports.log"
date=$(date +"%Y/%m/%d %H:%M:%S")
mongoimport= $(mongoimport --uri 'mongodb://carlos:carlos@localhost:27017/football?authSource=admin' --collection matches --drop --type csv --columnsHaveTypes --fieldFile=/home/db/fields.txt --file "$data")

echo "[$date] Comienza el update de la base de datos" >> $logFile

if [ -f $data ]; then
        # mv $data "primer.csv"
        echo "Archivo $data antiguo eliminado" >> $logFile
else
        echo "No se encontro archivo $data anterior" >> $logFile
fi


if [ ! -f $PyScript ]; then
        echo "No se encontro el archivo $PyScript terminando el programa" >> $logFile
        exit 1
else
        echo "Se empieza a ejecutar $PyScript" >> $logFile
        python3 $PyScript > /dev/pts/5 2>&1
        sleep 5
fi


if [ ! -f "/root/matchesdata2022-2023.csv" ]; then
        echo "No se ha generado el archivo $data terminando el programa" >> $logFile
else
        mv /root/matchesdata2022-2023 $data
        echo "Archivo $data generado y Headerline borrado"
        sed -i '1d' "$data" #Elimina el Headerline
        $mongoimport 2> $logFile
        echo "Base de datos actualizada"
fi