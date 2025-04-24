from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

YT_VIDEO_ENDPOINT = 'https://www.youtube.com/watch?v='
YT_PLAYLIST_ENDPOINT = 'https://www.youtube.com/playlist?list='
YT_API_KEY = os.environ['YT_API_KEY']

youtube = build("youtube", "v3", developerKey=YT_API_KEY)



def search_album_track_on_yt(search_query):
    """Searches for an album on regular YT by filtering channels with 'Topic' phrase"""
    print(f'search_album_track_on_yt(search_query) function has been called')
    print(f'searchquery={search_query}')

    album_track_found = False
    artist_query, title_query = search_query.split(' ', 1)

    request = youtube.search().list(
        part='snippet',
        q=search_query,
        type='video',
        maxResults=50,
    )
    response = request.execute()

    yt_video_info = []

    for item in response['items']:

        if "Topic" in item['snippet']['channelTitle'] and title_query in item['snippet']['description']:
            print(item['snippet']['channelTitle'])
            print(title_query)
            print(item['snippet']['description'])
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']

            yt_video_info.append(
                {
                'YouTubeVideoTitle': video_title,
                'YouTubeVideoUrl': YT_VIDEO_ENDPOINT + video_id,
                'video_id': video_id,
                }
            )

            album_track_found = True
        else:
            pass
    print(f"search_album_track_on_yt response from YouTubeAPI: {response}")
    return album_track_found, yt_video_info


def search_playlist_on_yt(search_query):
    """Searches for playlists on regular YT"""
    print('search_playlist_on_yt(searchquery) function has been called')
    print(f'searchquery={search_query}')

    yt_playlist_found = False

    artist_query, title_query = search_query.split(' ', 1)

    request = youtube.search().list(part='snippet', q=search_query)
    response = request.execute()

    yt_playlist_info = []

    for item in response['items']:

        if item['id']['kind'] == 'youtube#playlist':
            playlist_id = item['id']['playlistId']

            playlist_request = youtube.playlists().list(part="snippet", id=playlist_id)
            playlist_response = playlist_request.execute()

            if 'items' in playlist_response:
                yt_playlist_found = True

                playlist_title = playlist_response['items'][0]['snippet']['title']

                playlist_items_request = youtube.playlistItems().list(
                    part="contentDetails,snippet",
                    playlistId=playlist_id,
                    maxResults=50
                )
                playlist_items_response = playlist_items_request.execute()

                playlist_tracks = []

                video_num = 0

                for item in playlist_items_response['items']:
                    video_num += 1

                    video_id = item['contentDetails']['videoId']
                    video_title = item['snippet']['title']
                    video_url = YT_VIDEO_ENDPOINT + video_id

                    playlist_tracks.append(
                        {
                            "video_num": video_num,
                            "video_title": video_title,
                            "video_url": video_url,
                            "video_id": video_id,
                        }
                    )

                yt_playlist_info.append(
                    {
                        'YouTubePlaylistTitle': playlist_title,
                        'YouTubePlaylistUrl': YT_PLAYLIST_ENDPOINT + playlist_id,
                        'yt_playlist_tracklist': playlist_tracks,
                    }
                )
    print(f"search_playlist_on_yt response from YouTubeAPI: {response}")
    return yt_playlist_found, yt_playlist_info


def search_video_on_yt(search_query):
    """Searches for a video on regular YT"""
    print('search_video_on_yt(search_query) function has been called')
    print(f'searchquery={search_query}')

    video_found = False
    yt_video_info = []

    try:
        artist_query, title_query = search_query.split(' ', 1)
    except ValueError:
        artist_query, title_query = search_query, ""

    request = youtube.search().list(
        part='snippet',
        q=search_query,
        type='video',
        maxResults=15,
    )

    try:
        response = request.execute()
    except Exception as e:
        print(f"Error during YouTube API request: {e}")
        return video_found, yt_video_info

    for item in response.get('items', []):
        try:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']

            yt_video_info.append({
                'YouTubeVideoTitle': video_title,
                'YouTubeVideoUrl': YT_VIDEO_ENDPOINT + video_id,
                'video_id': video_id,
            })

            video_found = True
        except (KeyError, TypeError) as e:
            print(f"Skipping item due to missing videoId or title: {e}")
            continue

    print(f"search_video_on_yt(search_query) response from YouTubeAPI: {response}")
    return video_found, yt_video_info


