from flask import render_template, session

def audio_player():
    video_id = session.get('video_id')
    return render_template('player.html', video_id=video_id)