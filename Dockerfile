FROM python:3.12-alpine

COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

WORKDIR /app

RUN set -e; addgroup -S api --gid=1000; adduser -S --ingroup api --uid=1000 api;
COPY entrypoint.sh entrypoint.sh
COPY src .
# Temp - copy in sqlite db file for testing
# COPY ./src/instance/db.sqlite3 ./db.sqlite3 

RUN chown -R api:api .


USER api:api

EXPOSE 8080

CMD ["/bin/sh", "entrypoint.sh"]