import json
import log


# XXX This functions should be wrap by class.

def judge(message):
    log.logger().info(message)
    message.ack()


def label_of(dom):
    """タグ使用割合をもとにラベルを返す"""
    return "old"


def parse(msg):
    """Pub/Subメッセージのパースをする"""
    # XXX Should be parse to some object not to directory?
    return json.loads(msg)


def publish(url, label):
    """Pub/Sumに判定結果をパブリッシュする"""
    # XXX Cloud Pub/Sub client shoud be inject by constructor.
    pass


def store_to_bigquery(url, label):
    """BigQueryに判定結果を保存する"""
    # XXX BigQuery client shoud be inject by constructor.
    pass
