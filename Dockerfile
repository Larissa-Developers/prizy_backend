FROM python:3.6

RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev
RUN apt-get install -y net-tools
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /server

COPY ./ /server/

RUN mkdir -p /server/logs

RUN pip install pipenv
RUN pipenv install

EXPOSE 8000
