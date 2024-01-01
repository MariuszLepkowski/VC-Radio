import unittest
from unittest.mock import MagicMock, patch
from discography_downloader import DiscographyDownloader


class TestDiscographyDownloader(unittest.TestCase):

    def test_download_page(self):
        base_url = "https://example.com/"
        downloader = DiscographyDownloader(base_url)
        response_mock = MagicMock()
        response_mock.json.return_value = {"albums": [{"title": "Album 1"}]}

        with patch("requests.get", return_value=response_mock):
            result = downloader.download_page(1)

        expected_result = {"albums": [{"title": "Album 1"}]}
        self.assertEqual(result, expected_result)
