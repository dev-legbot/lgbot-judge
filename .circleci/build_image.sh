#!/bin/sh -eux

function build_push_docker_image() {
  local docker_tag=gcr.io/${PROJECT_ID}/${IMAGE_NAME}
  local tag=$(echo ${CIRCLE_SHA1} | cut -c 1-7)
  gcloud docker -- build -t ${docker_tag} -t ${docker_tag}:${tag} .
}

cd $(dirname $0)/..
build_push_docker_image
