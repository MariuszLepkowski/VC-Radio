import pytest
from unittest.mock import patch


@pytest.fixture
def mock_yt_api_response():
    """Mock response from YouTube API for both search_album_track_on_yt and search_playlist_on_yt"""
    return {
        "kind": "youtube#searchListResponse",
        "etag": "sample_etag",
        "nextPageToken": "CDIQAA",
        "regionCode": "PL",
        "pageInfo": {
            "totalResults": 2162,
            "resultsPerPage": 50
        },
        "items": [
            # Mock response for search_album_track_on_yt
            {
                "kind": "youtube#searchResult",
                "etag": "sample_etag_1",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "4f3l0VtFhJk"
                },
                "snippet": {
                    "publishedAt": "2012-03-20T08:14:37Z",
                    "channelId": "UCEKNZ6Tr1QQcHbGn-Lzvnbw",
                    "title": "michael landau - the big black bear - organic instrumentals",
                    "description": "michael landau organic instrumentals album released in 2012 - the big black bear",
                    "thumbnails": {
                        "default": {"url": "https://i.ytimg.com/vi/4f3l0VtFhJk/default.jpg"},
                        "medium": {"url": "https://i.ytimg.com/vi/4f3l0VtFhJk/mqdefault.jpg"},
                        "high": {"url": "https://i.ytimg.com/vi/4f3l0VtFhJk/hqdefault.jpg"}
                    },
                    "channelTitle": "Michael Landau - Topic",
                    "liveBroadcastContent": "none",
                    "publishTime": "2012-03-20T08:14:37Z"
                }
            },
            # Mock response for search_playlist_on_yt
            {
                "kind": "youtube#searchResult",
                "etag": "sample_etag_2",
                "id": {
                    "kind": "youtube#playlist",
                    "playlistId": "PLtlNFtEji3_hWVTi3Sj1ZfSqpf0sMasjy"
                },
                "snippet": {
                    "publishedAt": "2023-08-12T16:33:38Z",
                    "channelId": "UC_XLBsf2yvLmnpMQpo9iNiw",
                    "title": "The Michael Landau Group - Organic Instrumentals [FullAlbum]",
                    "description": "Year (2012) Quality [320Kb]",
                    "thumbnails": {
                        "default": {"url": "https://i.ytimg.com/vi/AT5Mzf98kls/default.jpg"},
                        "medium": {"url": "https://i.ytimg.com/vi/AT5Mzf98kls/mqdefault.jpg"},
                        "high": {"url": "https://i.ytimg.com/vi/AT5Mzf98kls/hqdefault.jpg"}
                    },
                    "channelTitle": "Musifyier",
                    "liveBroadcastContent": "none",
                    "publishTime": "2023-08-12T16:33:38Z"
                }
            }
        ]
    }


@pytest.fixture
def mock_playlist_response():
    """Mock response for YouTube API playlist details request"""
    return {
        "kind": "youtube#playlistListResponse",
        "etag": "sample_etag_playlist",
        "items": [
            {
                "kind": "youtube#playlist",
                "etag": "sample_etag_playlist_item",
                "id": "PLtlNFtEji3_hWVTi3Sj1ZfSqpf0sMasjy",
                "snippet": {"title": "The Michael Landau Group - Organic Instrumentals [FullAlbum]"}
            }
        ]
    }


@pytest.fixture
def mock_playlist_items_response():
    """Mock response for YouTube API playlist items request"""
    return {
        "kind": "youtube#playlistItemListResponse",
        "etag": "sample_etag_playlist_items",
        "items": [
            {
                "kind": "youtube#playlistItem",
                "etag": "sample_etag_playlist_item_1",
                "contentDetails": {"videoId": "AT5Mzf98kls"},
                "snippet": {"title": "Delano"}
            },
            {
                "kind": "youtube#playlistItem",
                "etag": "sample_etag_playlist_item_2",
                "contentDetails": {"videoId": "4DX26tU6WLs"},
                "snippet": {"title": "Ghouls And The Goblins"}
            }
        ]
    }


@pytest.fixture
def mock_youtube_search(mock_yt_api_response, mock_playlist_response, mock_playlist_items_response):
    """Mocks youtube.search().list().execute() and related API calls"""
    with patch("VC_Radio_app.utils.yt_search_utils.youtube.search") as mock_search, \
            patch("VC_Radio_app.utils.yt_search_utils.youtube.playlists") as mock_playlists, \
            patch("VC_Radio_app.utils.yt_search_utils.youtube.playlistItems") as mock_playlist_items:
        # Mock search().list().execute()
        mock_request = mock_search.return_value.list.return_value
        mock_request.execute.return_value = mock_yt_api_response

        # Mock playlists().list().execute()
        mock_playlists_request = mock_playlists.return_value.list.return_value
        mock_playlists_request.execute.return_value = mock_playlist_response

        # Mock playlistItems().list().execute()
        mock_playlist_items_request = mock_playlist_items.return_value.list.return_value
        mock_playlist_items_request.execute.return_value = mock_playlist_items_response

        yield mock_search
