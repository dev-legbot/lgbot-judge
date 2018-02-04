import json


class Callback(object):
    def __init__(self, injector):
        self._logger = injector.logger()

    def callback(self, message):
        html_data = self.parse(message.data)
        self._logger.info(html_data)
        message.ack()

    def label_of(self, dom):
        """タグ使用割合をもとにラベルを返す"""
        return "old"

    def parse(self, data):
        """Pub/Subメッセージのパースをする"""
        return json.loads(data)

    def publish(self, url, label):
        """Pub/Sumに判定結果をパブリッシュする"""
        # XXX Cloud Pub/Sub client shoud be inject by constructor.
        pass

    def store_to_bigquery(self, url, label):
        """BigQueryに判定結果を保存する"""
        # XXX BigQuery client shoud be inject by constructor.
        pass
