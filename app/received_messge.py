import exceptions


class ReceivedMessage(object):
    """Values class of message is received from cloud pub/sub

    Attributes:
        url(str): url of message.
        doms(dict): dom dictionary.
    """

    def from_dict(message_dict={}):
        """Create ReceiveMessage object from Pub/Sub message dict.

        Args:
            message_dict (dict): Dict of Pub/Sub message

        Returns:
            The object of ReceiveMessage

        Raises:
            exceptions.InvalidMessageException: The message_dict is not valid.
        """
        h = ReceivedMessage(message_dict)
        h.validate()
        return h

    def __init__(self, message_dict={}):
        """Create new object

        Attributes:
            message_dict(dict): Dict of Pub/Sub message
        """
        self.url = message_dict.get("url", "")
        self.doms = message_dict.get("doms", [])

    def validate(self):
        """Check self attributes is valid.

        Raises:
            exceptions.InvalidMessageException: `url` or `doms` attributes is empty.
        """
        errs = []
        if not self.url.strip():
            errs.append("'url' is required parameter")
        if len(self.doms) == 0:
            errs.append("'doms' should include at least one tag")
        if len(errs) != 0:
            msg = ";".join(errs)
            raise exceptions.InvalidMessageException(msg)

    def __str__(self):
        return "URL: {}, DOMS: {}".format(self.url, self.doms)
