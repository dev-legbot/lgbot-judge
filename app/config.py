import os


PROJECT_ID = os.environ["PROJECT_ID"]
_TOPIC_NAME = os.environ["TOPIC_NAME"]
_SUBSCRIPTION_NAME = os.environ["SUBSCRIPTION_NAME"]
TOPIC = "projects/{}/topics/{}".format(PROJECT_ID, _TOPIC_NAME)
SUBSCRIPTION = "projects/{}/subscriptions/{}".format(PROJECT_ID, _SUBSCRIPTION_NAME)
