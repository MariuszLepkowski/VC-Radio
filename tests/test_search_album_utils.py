import pytest
from unittest.mock import patch, MagicMock
from VC_Radio_app.utils.search_album_utils import search_album


@pytest.fixture
def mock_discography_downloader():
    """Mock for DiscographyDownloader with a sample album"""
    with patch("VC_Radio_app.utils.search_album_utils.discography_downloader") as mock_downloader:
        mock_downloader.pick_random_album.return_value = {
            "artist": "Michael Landau",
            "album_title": "Organic Instrumentals"
        }
        yield mock_downloader


@pytest.fixture
def mock_yt_search_utils():
    """Mock YouTube search utilities"""
    with patch("VC_Radio_app.utils.search_album_utils.search_album_track_on_yt") as mock_track, \
            patch("VC_Radio_app.utils.search_album_utils.search_video_on_yt") as mock_video, \
            patch("VC_Radio_app.utils.search_album_utils.search_playlist_on_yt") as mock_playlist:
        mock_track.return_value = {"videoId": "4f3l0VtFhJk", "title": "The Big Black Bear"}
        mock_video.return_value = {"videoId": "XYZ123ABC456", "title": "Michael Landau - Live"}
        mock_playlist.return_value = {"playlistId": "PLtlNFtEji3_hWVTi3Sj1ZfSqpf0sMasjy", "title": "Full Album"}

        yield mock_track, mock_video, mock_playlist


def test_search_album_success(mock_discography_downloader, mock_yt_search_utils):
    """Test search_album() with valid YouTube search results"""
    picked_album, search_results = search_album()

    assert picked_album["artist"] == "Michael Landau"
    assert picked_album["album_title"] == "Organic Instrumentals"

    assert search_results["yt_album_track"] is not None
    assert search_results["yt_video"] is not None
    assert search_results["yt_playlist"] is not None

    assert search_results["yt_album_track"]["videoId"] == "4f3l0VtFhJk"
    assert search_results["yt_video"]["videoId"] == "XYZ123ABC456"
    assert search_results["yt_playlist"]["playlistId"] == "PLtlNFtEji3_hWVTi3Sj1ZfSqpf0sMasjy"


def test_search_album_index_error(mock_discography_downloader):
    """Test search_album() handling IndexError"""
    with patch("VC_Radio_app.utils.search_album_utils.search_album_track_on_yt", side_effect=IndexError):
        picked_album, search_results = search_album()

        assert picked_album["artist"] == "Michael Landau"
        assert picked_album["album_title"] == "Organic Instrumentals"

        assert search_results["yt_album_tracks"] is None
        assert search_results["yt_video"] is None
        assert search_results["yt_playlist"] is None
