class PubSub(object):
    def __init__(self, injector):
        self._publisher_client = injector.publisher_client()
        self._subscriber_client = injector.subscriber_client()
        self._logger = injector.logger(__name__)

    def publish(self, topic_name, message, attribute={}):
        self._publisher_client.publish(
            topic_name, str.encode(message), **attribute)

    def subscribe(self, subscription_name, callback):
        subscription = self._subscriber_client.subscribe(subscription_name)
        feature = subscription.open(callback)

        try:
            feature.result()
        except BaseException as ex:
            self._logger.error(ex)
