import unittest

import pubsub

from unittest.mock import MagicMock


class TestPubSub(unittest.TestCase):
    def test_publish(self):
        client_mock = MagicMock()
        ps = pubsub.PubSub(MagicMock(), client_mock, MagicMock())
        ps.publish(
            topic_name="topic", message="message", attribute={"foo": "bar"}
        )
        client_mock.publish.assert_called_with(
            "topic", str.encode("message"), **{"foo": "bar"}
        )

    def test_subscribe(self):
        client_mock = MagicMock()
        subscribe_mock = MagicMock()
        future_mock = MagicMock()
        subscribe_mock.open.return_value = future_mock
        client_mock.subscribe.return_value = subscribe_mock

        ps = pubsub.PubSub(MagicMock(), MagicMock(), client_mock)
        callback_mock = MagicMock()
        ps.subscribe("subscribe", callback_mock)

        client_mock.subscribe.assert_called_with("subscribe")
        subscribe_mock.open.assert_called_with(callback_mock)
        future_mock.result.assert_called()
