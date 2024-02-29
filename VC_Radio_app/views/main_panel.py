from flask import Blueprint, render_template
from VC_Radio_app.utils.search_album_utils import search_album


main_panel_blueprint = Blueprint('main_panel', __name__)


@main_panel_blueprint.route('/', methods=['GET', 'POST'])
def main_panel():
    album, results = search_album()
    return render_template('main-panel.html', album=album, results=results)