#!/bin/sh -eu

cd $(dirname $0)/..
python -m unittest discover
