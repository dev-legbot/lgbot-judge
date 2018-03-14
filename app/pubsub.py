class PubSub(object):
    def __init__(self, logger, publisher_client, subscriber_client):
        self._logger = logger
        self._publisher_client = publisher_client
        self._subscriber_client = subscriber_client

    def publish(self, topic_name, message, attribute={}):
        """Publish message to topic

        Args:
            topic_name(str): Topic name publish to.
            message(str): Publish message.
            attribute(dic): Publish attribute.
        """
        self._publisher_client.publish(
            topic_name, str.encode(message), **attribute
        )

    def subscribe(self, subscription_name, callback):
        """Subscribe site analyze message

        Args:
            subscription_name(str): Subscription name receive message from.
            callback(Callable): Callback function handle message.
        """
        subscription = self._subscriber_client.subscribe(subscription_name)
        feature = subscription.open(callback)

        try:
            feature.result()
        except BaseException as ex:
            self._logger.error(ex)
