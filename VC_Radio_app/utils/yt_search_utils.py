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
    print('search_video_on_yt')

    album_track_found = False
    print(f'searchquery={search_query}')

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

    return album_track_found, yt_video_info


def search_playlist_on_yt(search_query):
    """Searches for playlists on regular YT"""
    print('search_playlist_on_yt')

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

    return yt_playlist_found, yt_playlist_info


def search_video_on_yt(search_query):
    """Searches for a video on regular YT"""
    print('search_video_on_yt')

    video_found = False

    artist_query, title_query = search_query.split(' ', 1)

    request = youtube.search().list(
        part='snippet',
        q=search_query,
        type='video',
        maxResults=15,
    )
    response = request.execute()

    yt_video_info = []

    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']

        yt_video_info.append(
            {
            'YouTubeVideoTitle': video_title,
            'YouTubeVideoUrl': YT_VIDEO_ENDPOINT + video_id,
            'video_id': video_id,
            }
        )

        video_found = True

    return video_found, yt_video_info


# def search_album_on_ytmusic(search_query):
#     """Searches for each individual track on the requested album on YT Music"""
#
#     print('search_album_on_ytmusic')
#
#     album_found = False
#
#     artist_query, title_query = search_query.split(' ', 1)
#
#     search_results = yt.search(query=search_query, filter='albums')
#
#     ytmusic_album_info = []
#
#     unique_album_titles = set()
#
#     for result in search_results:
#         album_artist = result['artists'][1]['name']
#         album_title = result['title']
#
#         if all(word.lower() in album_artist.lower() for word in artist_query.lower().split()) or all(
#                 word in album_title.lower().split() for word in title_query.lower().split()):
#
#             if album_title not in unique_album_titles:
#                 album_found = True
#                 unique_album_titles.add(album_title)
#
#                 album_browseId = result['browseId']
#
#                 try:
#                     album_info = yt.get_album(browseId=album_browseId)
#                 except ValueError as e:
#                     print(f"Error while processing album: {e}")
#                     continue
#
#                 album_tracklist = album_info['tracks']
#
#                 album_data = {
#                     'ytMusicAlbumTitle': album_title,
#                     'ytMusicAlbumArtist': album_artist,
#                     'AlbumTracklist': []
#                 }
#
#                 for track in album_tracklist:
#                     album_data['AlbumTracklist'].append(
#                         {
#                             'trackNumber': track['trackNumber'],
#                             'trackTitle': track['title'],
#                             'trackURL': YT_VIDEO_ENDPOINT + track['videoId'] if track.get('videoId') else "",
#                             'video_id': track['videoId'] if track.get('videoId') else "",
#                         }
#                     )
#
#                 ytmusic_album_info.append(album_data)
#
#     return album_found, ytmusic_album_info
#
#
# def search_playlist_on_ytmusic(search_query):
#     """Searches for playlists on YT Music"""
#     print('search_playlist_on_ytmusic')
#
#     ytm_playlist_found = False
#
#     artist_query, title_query = search_query.split(' ', 1)
#
#     search_results = yt.search(search_query, filter='playlists')
#
#     ytmusic_playlist_info = []
#
#     for result in search_results:
#         playlist_title_wordlist = result['title'].lower().split()
#
#         if all(word in playlist_title_wordlist for word in artist_query.lower().split()) or all(
#                 word in playlist_title_wordlist for word in title_query.lower().split()):
#             ytm_playlist_found = True
#
#             try:
#                 playlist_info = yt.get_playlist(playlistId=result['browseId'])
#             except ValueError as e:
#                 print(f"Error while processing playlist: {e}")
#                 continue
#
#             playlist_tracklist = playlist_info.get('tracks', [])
#             playlist_tracks = []
#
#             track_num = 0
#
#             for track in playlist_tracklist:
#                 track_num += 1
#                 track_title = track['title']
#                 if 'videoId' in track and track['videoId'] is not None:
#                     track_url = YT_VIDEO_ENDPOINT + track['videoId']
#                     playlist_tracks.append(
#                         {
#                             'trackNumber': track_num,
#                             'trackTitle': track_title,
#                             'trackURL': track_url,
#                             'video_id': track['videoId'],
#                         }
#                     )
#                 else:
#                     print("Warning: Missing or invalid videoId for track. Skipping...")
#
#             ytmusic_playlist_info.append(
#                 {
#                     'ytMusicPlaylistTitle': result['title'],
#                     'ytMusicPlaylistURL': YT_PLAYLIST_ENDPOINT + playlist_info['id'],
#                     'PlaylistTracklist': playlist_tracks,
#                 }
#             )
#
#     return ytm_playlist_found, ytmusic_playlist_info
