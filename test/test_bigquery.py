import bigquery
import unittest

from unittest.mock import MagicMock


class TestBigQuery(unittest.TestCase):
    def test_insert_judge_result(self):
        client_mock = MagicMock()
        table_mock = "table"

        cb = bigquery.BigQuery(client_mock, table_mock)
        cb.insert_judge_result("url", "label")

        client_mock.insert_rows.assert_called_with(
            table_mock, [("url", "label")]
        )


if __name__ == '__main__':
    unittest.main()
