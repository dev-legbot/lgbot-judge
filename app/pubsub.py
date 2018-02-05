class PubSub(object):
    def __init__(self, injector):
        self._publisher_client = injector.publisher_client()
        self._subscriber_client = injector.subscriber_client()
        self._logger = injector.logger()

    def create_topic(self, topic_name):
        self._publisher_client.create_topic(topic_name)

    def create_subscription(self, topic_name, subscription_name):
        self._subscriber_client.create_subscription(
            subscription_name, topic_name,
        )

    def publish(self, topic_name, message, attribute={}):
        self._publisher_client.publigh(
            topic_name, str.encode(message), **attribute)

    def subscribe(self, subscription_name, callback):
        subscription = self._subscriber_client.subscribe(subscription_name)
        feature = subscription.open(callback)

        try:
            feature.result()
        except BaseException as ex:
            self._logger.error(ex)
