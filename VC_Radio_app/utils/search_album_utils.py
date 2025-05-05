from VC_discography_scraper.discography_downloader import DiscographyDownloader
from VC_Radio_app.utils.yt_search_utils import search_video_on_yt, search_playlist_on_yt, search_album_track_on_yt

discography_downloader = DiscographyDownloader("https://vinniecolaiuta.com/Home/GetPageOfRecordings?page=")

def search_album():
    print("Downloading and saving discography...")
    picked_album = discography_downloader.pick_random_album()
    search_query = picked_album['artist'] + ' ' + picked_album['album_title']
    try:
        album_track_found = search_album_track_on_yt(search_query)
        video_found = search_video_on_yt(search_query)
        yt_playlist_found = search_playlist_on_yt(search_query)

        search_results_info = {
            "yt_album_track": album_track_found,
            "yt_playlist": yt_playlist_found,
            "yt_video": video_found,
        }
    except IndexError:
        print("An error occurred.")
        search_results_info = {
            "yt_album_tracks": None,
            "yt_playlist": None,
            "yt_video": None,
        }
    return picked_album, search_results_info
