import unittest
from unittest.mock import patch

from src.disk_check import check_disk_usage


class TestDiskCheck(unittest.TestCase):

    @patch("src.disk_check.shutil.disk_usage")
    def test_check_disk_usage(self, mock_disk_usage):
        mock_disk_usage.return_value = (1000, 400, 600)

        result = check_disk_usage("/")

        self.assertEqual(result["total"], 1000)
        self.assertEqual(result["used"], 400)
        self.assertEqual(result["free"], 600)
        self.assertEqual(result["usage_percent"], 40.0)

        mock_disk_usage.assert_called_once_with("/")


if __name__ == "__main__":
    unittest.main()
