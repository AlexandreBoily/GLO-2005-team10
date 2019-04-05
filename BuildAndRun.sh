#!/bin/bash
docker stop team10
docker rm team10
docker build -t team10 .
docker run -d -p 8080:8080 --rm --name team10 team10