#!/bin/bash
docker build --tag=math_ai .
docker run -d -p 13347:13347 --rm --name=math_ai math_ai
