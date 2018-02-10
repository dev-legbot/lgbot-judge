import json

from exceptions import InvalidMessageException
from receive_messge import ReceiveMessage


class Callback(object):
    def __init__(self, injector):
        self._logger = injector.logger()

    def callback(self, message):
        try:
            html_data = self.parse(message.data)
            self._logger.info(html_data)
            message.ack()
        except InvalidMessageException as ex:
            self._logger.warning("Invalid message : %s", ex)
        except Exception as ex:
            self._logger.error("Some error raises : %s", ex)

    def label_of(self, dom):
        """タグ使用割合をもとにラベルを返す"""
        return "old"

    def parse(self, data):
        """Parse json string to ReceiveMessage object

        Args:
            data(str): JSON string.

        Raises:
            exceptions.InvalidMessageException: Failed to parse message.
        """
        parsed_data = json.loads(data)
        return ReceiveMessage.from_dict(parsed_data)

    def publish(self, url, label):
        """Pub/Sumに判定結果をパブリッシュする"""
        # XXX Cloud Pub/Sub client shoud be inject by constructor.
        pass

    def store_to_bigquery(self, url, label):
        """BigQueryに判定結果を保存する"""
        # XXX BigQuery client shoud be inject by constructor.
        pass
