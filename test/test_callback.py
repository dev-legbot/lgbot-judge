import callback
import injector
import log
import unittest

from exceptions import InvalidMessageException
from received_messge import ReceivedMessage
from unittest.mock import MagicMock


class TestCallback(unittest.TestCase):
    def new_callback(i_mock=injector.Injector()):
        l_mock = log.Logger()
        i_mock.logger = MagicMock(return_value=l_mock)
        return callback.Callback(i_mock)

    def test_callback(self):
        l_mock = log.Logger()
        l_mock.info = MagicMock()
        i_mock = injector.Injector()
        i_mock.logger = MagicMock(return_value=l_mock)
        cb = callback.Callback(i_mock)

        parse_mock = MagicMock(return_value="parsed")
        cb.parse = parse_mock

        msg_mock = MagicMock()
        msg_mock.data = "test"

        cb.callback(msg_mock)

        parse_mock.assert_called_with("test")
        l_mock.info.assert_called_with("parsed")
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


if __name__ == '__main__':
    unittest.main()
