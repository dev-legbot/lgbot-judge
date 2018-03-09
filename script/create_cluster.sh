#!/bin/sh -eux

gcloud beta container --project ${PROJECT_ID} clusters create "lgbot-judge" \
  --zone "us-central1-a" \
  --no-enable-basic-auth \
  --cluster-version "1.9.2-gke.1" \
  --machine-type "g1-small" \
  --image-type "COS" \
  --disk-size "10" \
  --scopes "https://www.googleapis.com/auth/bigquery","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/pubsub","https://www.googleapis.com/auth/trace.append" \
  --preemptible \
  --num-nodes "1" \
  --network "default" \
  --enable-cloud-logging \
  --enable-cloud-monitoring \
  --subnetwork "default"
