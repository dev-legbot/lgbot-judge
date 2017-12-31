import callback
import log

from google.cloud import pubsub


def create_topic(topic):
    publisher = pubsub.PublisherClient()
    publisher.create_topic(topic)


def create_subscription(topic, subscription):
    subscriber = pubsub.SubscriberClient()
    subscriber.create_subscription(subscription, topic)


def publish(topic, message, attribute={}):
    publisher = pubsub.PublisherClient()
    publisher.publish(topic, str.encode(message), **attribute)


def subscribe(subsc):
    subscriber = pubsub.SubscriberClient()
    sub = subscriber.subscribe(subsc)
    feature = sub.open(callback.judge)
    try:
        feature.result()
    except BaseException as ex:
        log.logger().error(ex)
        sub.close()
