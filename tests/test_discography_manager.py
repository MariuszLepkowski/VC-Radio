import unittest
from unittest.mock import patch, Mock
from discography_manager import download_discography


class TestDownloadDiscography(unittest.TestCase):

    @patch("discography_manager.r.get", side_effect=[
        Mock(json=lambda: [
            {"$id": "1", "id": 2691, "year": "2023", "artist": "TestArtist1", "title": "TestAlbum1", "url": "https://test"},
            {"$id": "2", "id": 2690, "year": "2023", "artist": "TestArtist2", "title": "TestAlbum2", "url": "https://test"}
        ]),
        Mock(json=lambda: [])
    ])
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_download_discography(self, mock_open, mock_get):
        print("Before calling download_discography")
        download_discography()
        print("After calling download_discography")

        mock_open.assert_called_once_with("discography.csv", mode="a", encoding="utf-8")

if __name__ == '__main__':
    unittest.main()
