from flask import Blueprint, render_template, session

audio_player_blueprint = Blueprint('audio_player', __name__)


@audio_player_blueprint.route('/player')
def audio_player():
    video_id = session.get('video_id')
    return render_template('audio-player.html', video_id=video_id)

