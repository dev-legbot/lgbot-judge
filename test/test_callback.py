import callback
import config
import unittest

from pathlib import Path

from exceptions import InvalidMessageException
from received_messge import ReceivedMessage
from unittest.mock import MagicMock


class TestCallback(unittest.TestCase):
    def create_callback_with_mock(logger_mock=MagicMock(), pubsub_mock=MagicMock(), bigquery_mock=MagicMock()):
        return callback.Callback(logger_mock, pubsub_mock, bigquery_mock)

    def test_callback(self):
        cb = TestCallback.create_callback_with_mock()

        parsed_msg = ReceivedMessage(
            message_dict={"url": "http://xxx.com",
                          "doms": [{"tag": "div", "count": 1}]}
        )
        parse_mock = MagicMock(return_value=parsed_msg)
        cb._parse = parse_mock

        label_of_mock = MagicMock(return_value="old")
        cb._label_of = label_of_mock

        publish_mock = MagicMock()
        cb._publish = publish_mock

        msg_mock = MagicMock()
        msg_mock.data = "test"

        bigquery_mock = MagicMock()
        cb._store_to_bigquery = bigquery_mock

        cb.callback(msg_mock)

        parse_mock.assert_called_with("test")
        label_of_mock.assert_called_with(parsed_msg.doms)
        publish_mock.assert_called_with("http://xxx.com", "old")
        msg_mock.ack.assert_called()
        bigquery_mock.assert_called_with("http://xxx.com", "old")

    def test_label_of_old_site(self):
        cb = TestCallback.create_callback_with_mock()
        for old_site in old_site_testdatas():
            msg = ReceivedMessage.from_dict(old_site)
            got = cb._label_of(msg.doms)
            self.assertEqual(got, "old")

    def test_label_of_modern_site(self):
        cb = TestCallback.create_callback_with_mock()
        for modern_site in modern_site_testdatas():
            msg = ReceivedMessage.from_dict(modern_site)
            got = cb._label_of(msg.doms)
            self.assertEqual(got, "modern")

    def test_parse(self):
        cb = TestCallback.create_callback_with_mock()
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
            {"url": "http://xxx.com",
                "doms": [{"count": 1, "name": "div"}, {"count": 2, "name": "h1"}]}
        )
        got = cb._parse(msg)
        self.assertEqual(got.url, want.url)
        self.assertEqual(got.doms, want.doms)

    def test_parse_invalid_message(self):
        msg = '{"foo": "bar"}'
        cb = TestCallback.create_callback_with_mock()
        with self.assertRaises(InvalidMessageException):
            cb._parse(msg)

    def test_publish(self):
        pubsub_mock = MagicMock()
        cb = TestCallback.create_callback_with_mock(pubsub_mock=pubsub_mock)

        cb._publish("url", "old")

        pubsub_mock.publish.assert_called_with(
            config.TOPIC, "url", attribute={"label": "old"}
        )


def old_site_testdatas():
    old_site_dir = Path(".").joinpath("test/testdata/old")
    return read_all_file_in_directory(old_site_dir)


def modern_site_testdatas():
    modern_site_dir = Path(".").joinpath("test/testdata/modern")
    return read_all_file_in_directory(modern_site_dir)


def read_all_file_in_directory(path):
    import json
    files = [open(f) for f in path.iterdir()]
    datas = [json.loads(f.read()) for f in files]
    for f in files:
        f.close()
    return datas


if __name__ == '__main__':
    unittest.main()
