from VC_Radio_app import create_app
from VC_Radio_app.views.audio_player import audio_player_blueprint
from VC_Radio_app.views.search_album import search_album_blueprint


VC_Radio_app = create_app()
VC_Radio_app.register_blueprint(audio_player_blueprint)
VC_Radio_app.register_blueprint(search_album_blueprint)

if __name__ == "__main__":
    VC_Radio_app.run(debug=True, port=5000)
