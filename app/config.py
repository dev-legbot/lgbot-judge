import os


PROJECT_ID = os.environ["PROJECT_ID"]
_TOPIC_NAME = os.environ["TOPIC_NAME"]
_SUBSCRIPTION_NAME = os.environ["SUBSCRIPTION_NAME"]
TOPIC = "projects/{}/topics/{}".format(PROJECT_ID, _TOPIC_NAME)
SUBSCRIPTION = "projects/{}/subscriptions/{}".format(
    PROJECT_ID, _SUBSCRIPTION_NAME)

# サイト判定に使用するタグのリストと使用割合。
# 使用割合は、とりあえずサンプルサイトが全て判定可能なギリギリの値を設定
TAGS_FOR_JUDGE = ["td", "table", "tr", "br"]
TAG_USE_RATE_FOR_OLD_SITE = 0.19
