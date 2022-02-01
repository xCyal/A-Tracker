#Dockerfile

FROM python:3.8-slim

LABEL maintainer="xCyal <manuvilla444@gmail.com>"

WORKDIR /app

RUN groupadd -r trackergroup && useradd -m -r -g trackergroup trackeruser && chown -R trackeruser:trackergroup /app
USER trackeruser

ENV PATH = $PATH:/home/trackeruser/.local/bin

COPY poetry.lock pyproject.toml tasks.py /app/


# Opcion virtualenvs.create false para evitar que poetry genere otro entorno virtual dentro del propio contenedor
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

WORKDIR /app/test

ENTRYPOINT ["invoke","test"]
