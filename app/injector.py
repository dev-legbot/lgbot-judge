from callback import Callback
from pubsub import PubSub


class Injector(object):
    def callback():
        return Callback()

    def pubsub_client():
        return PubSub()
