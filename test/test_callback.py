import unittest

from app import callback
from test import helper


class MockInjector(object):
    def logger(self):
        return helper.MockLogger()


class TestCallback(unittest.TestCase):
    def setUp(self):
        self.callback = callback.Callback(MockInjector())

    def test_label_of(self):
        got = self.callback.label_of("hogehoge")
        self.assertEqual(got, "old")

    def test_parse(self):
        msg = '{"hoge": "fuga"}'
        got = self.callback.parse(msg)
        want = {"hoge": "fuga"}
        self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
