import pytest
from unittest.mock import patch
from VC_Radio_app.utils.yt_search_utils import search_album_track_on_yt
from VC_Radio_app.utils.yt_search_utils import YT_VIDEO_ENDPOINT


@pytest.fixture
def mock_youtube_search(mock_yt_api_response):
    """Mocks youtube.search().list().execute() to return data from mock_yt_api_response"""
    with patch("VC_Radio_app.utils.yt_search_utils.youtube.search") as mock_search:
        mock_request = mock_search.return_value.list.return_value
        mock_request.execute.return_value = mock_yt_api_response
        yield mock_search


def test_search_album_track_on_yt(mock_youtube_search):
    """Tests the correctness of album track search on YouTube"""
    search_query = "michael landau organic instrumentals"

    album_track_found, yt_video_info = search_album_track_on_yt(search_query)

    assert album_track_found is True
    assert len(yt_video_info) == 1
    assert yt_video_info[0]["YouTubeVideoTitle"] == "michael landau - the big black bear - organic instrumentals"
    assert yt_video_info[0]["YouTubeVideoUrl"] == f"{YT_VIDEO_ENDPOINT}4f3l0VtFhJk"
    assert yt_video_info[0]["video_id"] == "4f3l0VtFhJk"









