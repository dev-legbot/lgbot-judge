import config
import json

from exceptions import InvalidMessageException
from received_messge import ReceivedMessage


class Callback(object):
    def __init__(self, logger, pubsub_client, bigquery_client):
        self._logger = logger
        self._pubsub_client = pubsub_client
        self._bigquery_client = bigquery_client

    def callback(self, message):
        """Callback function receive message

        Args:
            message: Receive message.
        """
        try:
            html_data = self._parse(message.data)
            self._logger.info(html_data)
            label = self._label_of(html_data.doms)
            self._publish(html_data.url, label)
            message.ack()
            self._store_to_bigquery(html_data.url, label)
        except InvalidMessageException as ex:
            self._logger.warning("Invalid message : %s", ex)
        except Exception as ex:
            self._logger.error("Some error raises : %s", ex)

    def _label_of(self, dom):
        """Labeling site

        Args:
            dom(list): list of dom dictionary.

        Returns:
            lebal of dom.
             "old" or "modern"
        """
        # XXX 特定のタグの利用率のみでサイトタイプの判定をしている。
        #   * データ観察をして条件をチューニング
        #   * イケてるサイトの判定処理を加えて、 "どの程度イケてるか", "どの程度ダサいか" を割合で出す
        # ここらへんの修正が今後必要なはず。
        # また、将来的には機械学習で判定を行いたい。
        tag_cnt = sum([d["count"] for d in dom])
        judged_tag_counts = self._extract_tags_from_dom(
            dom=dom, tags=config.TAGS_FOR_JUDGE
        )
        judged_tag_sum = sum([d["count"] for d in judged_tag_counts])
        return "old" if judged_tag_sum / tag_cnt >= config.TAG_USE_RATE_FOR_OLD_SITE else "modern"

    def _parse(self, data):
        """Parse json string to ReceiveMessage object

        Args:
            data(str): JSON string.

        Raises:
            exceptions.InvalidMessageException: Failed to parse message.
        """
        parsed_data = json.loads(data)
        return ReceivedMessage.from_dict(parsed_data)

    def _publish(self, url, label):
        """Publish message to Pub/Sub topic

        Args:
            url(str): Site url.
            label(str): Site label.
        """
        self._pubsub_client.publish(
            config.TOPIC, url, attribute={"label": label}
        )

    def _extract_tags_from_dom(self, dom, tags):
        return list(filter(lambda d: d["name"] in tags, dom))

    def _store_to_bigquery(self, url, label):
        """Store results of judge to bigquery

        Args:
            url(str): Site url.
            label(str): Site label.
        """
        self._bigquery_client.insert_judge_result(url, label)
