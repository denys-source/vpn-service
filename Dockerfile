FROM python:3.11.3-alpine

WORKDIR /code/

COPY requirements.txt ./

RUN pip3 install -r ./requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .
