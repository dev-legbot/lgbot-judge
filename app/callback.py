import json


class Callback(object):
    def __init__(self, injector):
        self._logger = injector.logger()

    def callback(self, message):
        self._logger.info(message)
        message.ack()

    def label_of(self, dom):
        """タグ使用割合をもとにラベルを返す"""
        return "old"

    def parse(self, msg):
        """Pub/Subメッセージのパースをする"""
        # XXX Should be parse to some object not to directory?
        return json.loads(msg)

    def publish(self, url, label):
        """Pub/Sumに判定結果をパブリッシュする"""
        # XXX Cloud Pub/Sub client shoud be inject by constructor.
        pass

    def store_to_bigquery(self, url, label):
        """BigQueryに判定結果を保存する"""
        # XXX BigQuery client shoud be inject by constructor.
        pass
