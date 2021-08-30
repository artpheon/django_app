FROM debian:latest

LABEL name="Artur N."
LABEL maintainer="idcdtokms@gmail.com"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install wget sudo bash vim software-properties-common
    
RUN sudo apt-get -y install python3.9 python3.9-venv python3-pip python3.9-dev libpq-dev && \
    pip install --upgrade pip

WORKDIR /var/hrobbin

COPY ./src/* /var/hrobbin

RUN chmod 777 /var/hrobbin

EXPOSE 80

ENTRYPOINT /bin/bash start.sh