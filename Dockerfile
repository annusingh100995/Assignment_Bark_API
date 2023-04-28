FROM python:3.10.10

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt
