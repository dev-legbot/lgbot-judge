#!/bin/sh -eu

cd $(dirname $0)/..
export PYTHONPATH=$(pwd)/app:$(pwd)/test
python -m unittest discover
