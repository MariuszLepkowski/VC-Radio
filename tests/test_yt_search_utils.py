from VC_Radio_app.utils.yt_search_utils import search_album_track_on_yt, search_playlist_on_yt
from VC_Radio_app.utils.yt_search_utils import YT_VIDEO_ENDPOINT, YT_PLAYLIST_ENDPOINT


def test_search_album_track_on_yt(mock_youtube_search):
    """Tests the correctness of album track search on YouTube"""
    search_query = "michael landau organic instrumentals"

    album_track_found, yt_video_info = search_album_track_on_yt(search_query)

    assert album_track_found is True
    assert len(yt_video_info) == 1
    assert yt_video_info[0]["YouTubeVideoTitle"] == "michael landau - the big black bear - organic instrumentals"
    assert yt_video_info[0]["YouTubeVideoUrl"] == f"{YT_VIDEO_ENDPOINT}4f3l0VtFhJk"
    assert yt_video_info[0]["video_id"] == "4f3l0VtFhJk"


def test_search_playlist_on_yt(mock_youtube_search):
    """Test verifying correct playlist search behavior on YouTube"""
    search_query = "michael landau organic instrumentals"

    yt_playlist_found, yt_playlist_info = search_playlist_on_yt(search_query)

    assert yt_playlist_found is True
    assert len(yt_playlist_info) == 1
    assert yt_playlist_info[0]["YouTubePlaylistTitle"] == "The Michael Landau Group - Organic Instrumentals [FullAlbum]"
    assert yt_playlist_info[0]["YouTubePlaylistUrl"] == f"{YT_PLAYLIST_ENDPOINT}PLtlNFtEji3_hWVTi3Sj1ZfSqpf0sMasjy"

    assert len(yt_playlist_info[0]["yt_playlist_tracklist"]) == 2
    assert yt_playlist_info[0]["yt_playlist_tracklist"][0]["video_title"] == "Delano"
    assert yt_playlist_info[0]["yt_playlist_tracklist"][0]["video_id"] == "AT5Mzf98kls"
    assert yt_playlist_info[0]["yt_playlist_tracklist"][1]["video_title"] == "Ghouls And The Goblins"
    assert yt_playlist_info[0]["yt_playlist_tracklist"][1]["video_id"] == "4DX26tU6WLs"







