class MockLogger(object):
    def info(self, msg, *args, **keywards):
        self.msg = msg
        self.args = args
        self.keywards = keywards
