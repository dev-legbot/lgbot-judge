import callback
import injector
import log
import unittest

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
        got = cb.parse(msg)
        want = {
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
        got = cb.parse(msg)
        self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
