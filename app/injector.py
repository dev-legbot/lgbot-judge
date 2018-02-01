from google.cloud import pubsub

from callback import Callback
from log import Logger
from pubsub import PubSub


class Injector(object):
    def callback(self):
        return Callback(self)

    def pubsub_client(self):
        return PubSub(self)

    def logger(self):
        return Logger()

    def publisher_client(self):
        return pubsub.PublisherClient()

    def subscriber_client(self):
        return pubsub.SubscriberClient()
