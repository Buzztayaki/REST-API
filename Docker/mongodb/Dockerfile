# escape=`

FROM mongo:latest
RUN apt update && apt install -y sudo
RUN apt install cron
RUN apt install python3
RUN apt install pip
RUN pip install -r ./requirements.txt
RUN mkdir -p /home/db
WORKDIR /home/db
COPY ..\db\ /home/db/
EXPOSE 27017
