import log

from google.cloud import pubsub


class PubSub(object):
    def __init__(self):
        self.publisher_client = pubsub.PublisherClient()
        self.subscriber_client = pubsub.SubscriberClient()

    def create_topic(self, topic_name):
        self.publisher_client.create_topic(topic_name)

    def create_subscription(self, topic_name, subscription_name):
        self.subscriber_client.create_subscription(
            subscription_name, topic_name,
        )

    def publish(self, topic_name, message, attribute={}):
        self.publisher_client.publigh(
            topic_name, str.encode(message), **attribute)

    def subscribe(self, subscription_name, callback):
        subscription = self.subscriber_client.subscribe(subscription_name)
        feature = subscription.open(callback)

        try:
            feature.result()
        except BaseException as ex:
            log.logger().error(ex)
