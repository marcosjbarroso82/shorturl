FROM python:3.4
MAINTAINER ContextInformatic <contextinformatic@gmail.com>
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install libpq-dev python3-dev python3-pip

RUN mkdir -p /usr/src/app


WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip3 install -r /usr/src/app/requirements.txt --no-cache-dir

RUN chmod 777 /usr/src/app/init.sh
RUN chmod +x /usr/src/app/init.sh
