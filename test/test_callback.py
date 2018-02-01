import unittest

from app import callback


class TestCallback(unittest.TestCase):
    def setUp(self):
        self.callback = callback.Callback()

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
