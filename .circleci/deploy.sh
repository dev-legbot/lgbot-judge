#!/bin/sh -euv

cd $(dirname $0)/../

gcloud config set project ${PROJECT_ID}
gcloud container clusters get-credentials lgbot-judge --zone us-central1-a

tag=$(echo ${CIRCLE_SHA1} | cut -c 1-7)

sed -i -e "s/\${PROJECT_ID}/${PROJECT_ID}/g" k8s/deployment.yaml
sed -i -e "s/\${DOCKER_IMAGE}/gcr\.io\/${PROJECT_ID}\/${IMAGE_NAME}:${tag}/g" k8s/deployment.yaml
sed -i -e "s/\${SUBSCRIPTION_NAME}/${SUBSCRIPTION}/g" k8s/deployment.yaml
sed -i -e "s/\${TOPIC_NAME}/${TOPIC}/g" k8s/deployment.yaml
sed -i -e "s/\${BQ_DATASET}/${BQ_DATASET}/g" k8s/deployment.yaml
sed -i -e "s/\${BQ_TABLE}/${BQ_TABLE}/g" k8s/deployment.yaml

kubectl apply -f k8s/
