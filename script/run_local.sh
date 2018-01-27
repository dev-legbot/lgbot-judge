#!/bin/sh -eux

# Exec in local docker container
# Create Emulators Topic and Subscription, and listhen message.

echo "{}" > /tmp/key.json

sleep 5
python ../app/run.py prepare
