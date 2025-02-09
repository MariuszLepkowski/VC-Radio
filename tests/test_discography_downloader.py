import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from VC_discography_scraper.discography_downloader import DiscographyDownloader


@pytest.fixture
def downloader():
    """Fixture for DiscographyDownloader instance."""
    return DiscographyDownloader("https://vinniecolaiuta.com/Home/GetPageOfRecordings?page=")


@pytest.fixture
def mock_discography_response():
    """Mock JSON response from Vinnie Colaiuta's discography page."""
    return [
        {"year": "2021", "artist": "Bill Cunliffe, John Patitucci and Vinnie Colaiuta", "title": "Trio"},
        {"year": "2020", "artist": "Oz Noy", "title": "Snapdragon"},
    ]


@patch("VC_discography_scraper.discography_downloader.requests.get")
def test_download_page(mock_requests_get, downloader, mock_discography_response):
    """Test downloading a page from the discography."""
    mock_response = MagicMock()
    mock_response.json.return_value = mock_discography_response
    mock_requests_get.return_value = mock_response

    result = downloader.download_page(1)

    assert result == mock_discography_response
    mock_requests_get.assert_called_once_with("https://vinniecolaiuta.com/Home/GetPageOfRecordings?page=1")


@patch("VC_discography_scraper.discography_downloader.pd.DataFrame.to_csv")
def test_save_to_csv(mock_to_csv, downloader, mock_discography_response):
    """Test saving downloaded discography data to CSV."""
    downloader.save_to_csv(mock_discography_response)
    mock_to_csv.assert_called_once()


@patch("VC_discography_scraper.discography_downloader.DiscographyDownloader.download_page")
@patch("VC_discography_scraper.discography_downloader.DiscographyDownloader.save_to_csv")
def test_download_and_save_whole_discography(mock_save_to_csv, mock_download_page, downloader,
                                             mock_discography_response):
    """Test downloading and saving the entire discography."""
    mock_download_page.side_effect = [mock_discography_response, []]

    downloader.download_and_save_whole_discography()

    assert mock_download_page.call_count == 2
    mock_save_to_csv.assert_called_once_with(mock_discography_response)


@patch("VC_discography_scraper.discography_downloader.pd.read_csv")
@patch("VC_discography_scraper.discography_downloader.pd.DataFrame.sample")
def test_pick_random_album(mock_sample, mock_read_csv, downloader, mock_discography_response):
    """Test picking a random album from the discography CSV."""
    mock_read_csv.return_value = pd.DataFrame(mock_discography_response)
    mock_sample.return_value = pd.DataFrame([mock_discography_response[0]])

    result = downloader.pick_random_album()

    assert result["artist"] == "Bill Cunliffe, John Patitucci and Vinnie Colaiuta"
    assert result["album_title"] == "Trio"
    assert result["year"] == "2021"
