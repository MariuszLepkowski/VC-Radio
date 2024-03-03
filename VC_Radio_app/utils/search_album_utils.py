from VC_discography_scraper.discography_downloader import DiscographyDownloader
from VC_Radio_app.utils.yt_search_utils import search_album_on_ytmusic, search_playlist_on_ytmusic, search_video_on_yt, search_playlist_on_yt

discography_downloader = DiscographyDownloader("https://vinniecolaiuta.com/Home/GetPageOfRecordings?page=")

def search_album():
    print("Downloading and saving discography...")
    picked_album = discography_downloader.pick_random_album()
    search_query = picked_album['artist'] + ' ' + picked_album['album_title']
    try:
        album_found = search_album_on_ytmusic(search_query)
        ytm_playlist_found = search_playlist_on_ytmusic(search_query)
        video_found = search_video_on_yt(search_query)
        yt_playlist_found = search_playlist_on_yt(search_query)

        search_results_info = {
            "yt_music_album": album_found,
            "yt_music_playlist": ytm_playlist_found,
            "yt_video": video_found,
            "yt_playlist": yt_playlist_found
        }
    except IndexError:
        print("An error occurred.")
        search_results_info = {
            "yt_music_album": None,
            "yt_music_playlist": None,
            "yt_video": None,
            "yt_playlist": None
        }
    return picked_album, search_results_info
