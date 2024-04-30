FROM python:3.11.4-slim-bullseye


ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /synck

COPY . .

RUN ls

RUN apt-get update

RUN pip install -r ./requirements/requirements.txt

