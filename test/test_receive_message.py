import exceptions
import receive_messge
import unittest


class TestReceiveMessage(unittest.TestCase):
    def test_validate(self):
        data = {"url": "URL", "doms": [{"foo": "bar"}]}
        msg = receive_messge.ReceiveMessage(data)
        try:
            msg.validate()
        except Exception as ex:
            self.fail("raise exception : {}".format(ex))

    def test_validate_lackof_url(self):
        data = {"doms": [{"foo": "bar"}]}
        msg = receive_messge.ReceiveMessage(data)
        with self.assertRaises(exceptions.InvalidMessageException):
            msg.validate()

    def test_validate_lackof_doms(self):
        data = {"url": "URL"}
        msg = receive_messge.ReceiveMessage(data)
        with self.assertRaises(exceptions.InvalidMessageException):
            msg.validate()


if __name__ == '__main__':
    unittest.main()
