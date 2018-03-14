from google.cloud import bigquery

TABLE_SCHEMA = [
    bigquery.SchemaField("url", "STRING", mode="required"),
    bigquery.SchemaField("label", "STRING", mode="required"),
]


class BigQuery(object):
    def __init__(self, client, table):
        self._client = client
        self._table = table

    def insert_judge_result(self, url, label):
        """Insert judge result row to BigQuery

        Args:
            url(str): Site URL.
            label(str): Label of site.
        """
        rows = [(url, label)]
        self._client.insert_rows(self._table, rows)
