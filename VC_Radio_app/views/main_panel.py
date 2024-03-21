from flask import Blueprint, render_template, request
from VC_Radio_app.utils.search_album_utils import search_album


main_panel_blueprint = Blueprint('main_panel', __name__)


@main_panel_blueprint.route('/')
def main_panel():
    return render_template('main-panel.html')


@main_panel_blueprint.route('/about')
def about():
    return render_template('about.html')


@main_panel_blueprint.route('/album-generator', methods=['GET', 'POST'])
def album_generator():
    if request.method == 'POST':
        album, results = search_album()
    else:
        album = None
        results = None
    return render_template('album-generator.html', album=album, results=results)