FROM python:3.12-slim

MAINTAINER "projectsbytolokov@gmail.com"

LABEL maintainer="projectsbytolokov@gmail.com"

RUN apt-get update && pip install --upgrade pip

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code

COPY . /code

EXPOSE 8080

CMD ["python3", "main.py"]
