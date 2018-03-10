import bigquery as bq
import config

from google.cloud import bigquery
from google.cloud import pubsub

from callback import Callback
from log import Logger
from pubsub import PubSub


class Injector(object):
    def __init__(self):
        self._init_pubsub()
        self._init_bigquery()

    def bigquery(self):
        return bq.BigQuery(self._bigquery_client, self._table)

    def callback(self):
        return Callback(
            self.logger(Callback.__name__),
            self.pubsub(),
            self.bigquery(),
        )

    def logger(self, name):
        return Logger(name)

    def pubsub(self):
        return PubSub(
            self.logger(PubSub.__name__),
            self._publisher_client,
            self._subscriber_client,
        )

    def _init_pubsub(self):
        self._publisher_client = pubsub.PublisherClient()
        self._subscriber_client = pubsub.SubscriberClient()

    def _init_bigquery(self):
        self._bigquery_client = bigquery.Client()
        dataset_ref = self._bigquery_client.dataset(config.BQ_DATASET)
        dataset = bigquery.Dataset(dataset_ref)
        table_ref = dataset.table(config.BQ_TABLE)
        self._table = bigquery.Table(table_ref, bq.TABLE_SCHEMA)
