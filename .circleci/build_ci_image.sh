#!/bin/sh -eux

cd $(dirname $0)
docker build -t gcr.io/${PROJECT_ID}/lgbot-judge-builder .
