from flask import Blueprint, render_template, redirect, url_for, request, session
from YT_music_player.forms import UrlForm


url_blueprint = Blueprint('url', __name__)


def extract_video_id(video_url):
    """Extracts video_id from YouTube video url"""
    video_id_index = video_url.find('v=') + 2
    video_id = video_url[video_id_index:]
    return video_id


@url_blueprint.route('/url', methods=['GET', 'POST'])
def enter_url():
    form=UrlForm()

    if form.validate_on_submit():
        url = request.form['video_url']
        video_id = extract_video_id(url)
        session['video_id'] = video_id
        return redirect(url_for('audio_player.audio_player'))

    return render_template('url.html', form=form)
