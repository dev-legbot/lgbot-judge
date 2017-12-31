#!/bin/sh -eux

echo "{}" > /tmp/key.json
python /judge/app/run.py prepare
