# escape=`

FROM python:3.11.2-bullseye
RUN mkdir -p /var/api
WORKDIR /var/api
COPY ..\src\ /var/api/
EXPOSE 5000
RUN pip install -r ./requirements.txt