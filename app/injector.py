import config

from google.cloud import bigquery
from google.cloud import pubsub

from bigquery import BigQuery
from callback import Callback
from log import Logger
from pubsub import PubSub


class Injector(object):
    def __init__(self):
        self.__init_bigquery()

    def bigquery(self):
        return BigQuery(self.__bigquery_client, self.__table)

    def callback(self):
        return Callback(self)

    def logger(self):
        return Logger()

    def pubsub_client(self):
        return PubSub(self)

    def publisher_client(self):
        return pubsub.PublisherClient()

    def subscriber_client(self):
        return pubsub.SubscriberClient()

    def __init_bigquery(self):
        self.__bigquery_client = bigquery.Client()
        dataset_ref = self.__bigquery_client.Dataset(config.BQ_DATASET)
        dataset = bigquery.Dataset(dataset_ref)
        table_ref = dataset.table(config.BQ_TABLE)
        self.__table = bigquery.Table(table_ref)
