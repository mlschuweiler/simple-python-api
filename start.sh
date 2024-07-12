#!/bin/zsh

docker build -t simple-python-api:local .
docker run -it --rm -p 8080:8080 simple-python-api:local