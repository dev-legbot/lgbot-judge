#!/bin/sh

docker exec -it judge_app_1 python /judge/app/run.py publish "$1"
