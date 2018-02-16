import callback
import config
import unittest

from exceptions import InvalidMessageException
from received_messge import ReceivedMessage
from unittest.mock import MagicMock


class TestCallback(unittest.TestCase):
    def default_injector():
        return MagicMock()

    def new_callback():
        return callback.Callback(TestCallback.default_injector())

    def test_callback(self):
        cb = TestCallback.new_callback()

        parsed_msg = ReceivedMessage(message_dict={"url": "http://xxx.com", "doms": [{"tag": "div", "count": 1}]})
        parse_mock = MagicMock(return_value=parsed_msg)
        cb.parse = parse_mock

        label_of_mock = MagicMock(return_value="old")
        cb.label_of = label_of_mock

        publish_mock = MagicMock()
        cb.publish = publish_mock

        msg_mock = MagicMock()
        msg_mock.data = "test"
        cb.callback(msg_mock)

        parse_mock.assert_called_with("test")
        label_of_mock.assert_called_with(parsed_msg.doms)
        publish_mock.assert_called_with("http://xxx.com", "old")
        msg_mock.ack.assert_called()

    def test_label_of(self):
        cb = TestCallback.new_callback()
        got = cb.label_of("hogehoge")
        self.assertEqual(got, "old")

    def test_parse(self):
        cb = TestCallback.new_callback()
        msg = '''
        {
          "url": "http://xxx.com",
          "doms": [
            {
              "count": 1,
              "name": "div"
            },
            {
              "count": 2,
              "name": "h1"
            }
          ]
        }
        '''
        want = ReceivedMessage(
            {"url": "http://xxx.com", "doms": [{"count": 1, "name": "div"}, {"count": 2, "name": "h1"}]})
        got = cb.parse(msg)
        self.assertEqual(got.url, want.url)
        self.assertEqual(got.doms, want.doms)

    def test_parse_invalid_message(self):
        msg = '{"foo": "bar"}'
        cb = TestCallback.new_callback()
        with self.assertRaises(InvalidMessageException):
            cb.parse(msg)

    def test_publish(self):
        i_mock = TestCallback.default_injector()

        pubsub_mock = MagicMock()
        i_mock.pubsub_client = MagicMock(return_value=pubsub_mock)

        cb = callback.Callback(i_mock)
        cb.publish("url", "old")

        pubsub_mock.publish.assert_called_with(config.TOPIC, "url", attribute={"label": "old"})


if __name__ == '__main__':
    unittest.main()
