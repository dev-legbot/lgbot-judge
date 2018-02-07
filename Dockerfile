FROM ryutah/gcp-python

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt \
 && rm /tmp/requirements.txt

COPY . /judge

CMD ["python", "/judge/app/run.py", "default"]
