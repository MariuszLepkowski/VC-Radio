import pytest

@pytest.fixture
def mock_yt_api_response():
    """Mock YouTubeAPI response for testing."""
    return {
        "kind": "youtube#searchListResponse",
        "etag": "OqrmdwxNVHIDLVKUyHu_EHSHcDg",
        "nextPageToken": "CDIQAA",
        "regionCode": "PL",
        "pageInfo": {
            "totalResults": 2162,
            "resultsPerPage": 50
        },
        "items": [
            {
                "kind": "youtube#searchResult",
                "etag": "kwug8ozgGTBks5oKGL--y2eWxSI",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "4f3l0VtFhJk"
                },
                "snippet": {
                    "publishedAt": "2012-03-20T08:14:37Z",
                    "channelId": "UCEKNZ6Tr1QQcHbGn-Lzvnbw",
                    "title": "michael landau - the big black bear - organic instrumentals",
                    "description": "michael landau organic instrumentals album released in 2012 - the big black bear michael landau - guitar gary novak - drums ...",
                    "thumbnails": {
                        "default": {"url": "https://i.ytimg.com/vi/4f3l0VtFhJk/default.jpg", "width": 120, "height": 90},
                        "medium": {"url": "https://i.ytimg.com/vi/4f3l0VtFhJk/mqdefault.jpg", "width": 320, "height": 180},
                        "high": {"url": "https://i.ytimg.com/vi/4f3l0VtFhJk/hqdefault.jpg", "width": 480, "height": 360}
                    },
                    "channelTitle": "Michael Landau - Topic",
                    "liveBroadcastContent": "none",
                    "publishTime": "2012-03-20T08:14:37Z"
                }
            }
        ]
    }
