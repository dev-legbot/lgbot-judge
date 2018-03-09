class BigQuery(object):
    def __init__(self, client, table):
        self._client = client
        self._table = table

    def insert_judge_result(self, url, label):
        self._client.insert_rows(self._table, {"url": url, "label": label})
