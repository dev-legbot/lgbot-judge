FROM python:alpine3.7

ARG BUILD_DEPS="linux-headers alpine-sdk"

RUN apk add --no-cache ${BUILD_DEPS} \
 && rm -rf /tmp/*

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt \
 && rm /tmp/requirements.txt

COPY . /judge

CMD ["python", "/judge/app/run.py", "default"]
