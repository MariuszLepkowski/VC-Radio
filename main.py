
from YT_music_player import create_app as create_music_app
from VC_discography_scraper.discography_downloader import DiscographyDownloader
from YT_music_player.views.url import url_blueprint
from YT_music_player.views.audio_player import audio_player_blueprint

DISCOGRAPHY_URL = "https://vinniecolaiuta.com/Home/GetPageOfRecordings?page="

VC_music_player_app = create_music_app()
VC_music_player_app.register_blueprint(url_blueprint)
VC_music_player_app.register_blueprint(audio_player_blueprint)

# Run scraper
discography_downloader = DiscographyDownloader(DISCOGRAPHY_URL)
discography_downloader.pick_random_album()

if __name__ == "__main__":
    VC_music_player_app.run(debug=True, port=5000)
