#!/bin/sh -eu

cd $(dirname $0)/..
export PYTHONPATH=$(pwd)/app:$(pwd)/test
export PROJECT_ID=test_project
export TOPIC_NAME=test_topic
export SUBSCRIPTION_NAME=test_subscription
python -m unittest discover
