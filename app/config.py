import os


PROJECT_ID = os.environ["PROJECT_ID"]

TOPIC = "projects/{}/topics/{}".format(PROJECT_ID, os.environ["TOPIC_NAME"])
SUBSCRIPTION = "projects/{}/subscriptions/{}".format(
    PROJECT_ID, os.environ["SUBSCRIPTION_NAME"]
)

BQ_DATASET = os.environ["BQ_DATASET"]
BQ_TABLE = os.environ["BQ_TABLE"]


# サイト判定に使用するタグのリストと使用割合。
# 使用割合は、とりあえずサンプルサイトが全て判定可能なギリギリの値を設定
TAGS_FOR_JUDGE = ["td", "table", "tr", "br"]
TAG_USE_RATE_FOR_OLD_SITE = 0.19
