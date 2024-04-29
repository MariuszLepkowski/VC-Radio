from flask import Blueprint, render_template, request
from VC_Radio_app.utils.search_album_utils import search_album


main_panel_blueprint = Blueprint('main_panel', __name__)


def process_album_request():
    if request.method == 'POST':  # Jeśli formularz został wysłany
        return search_album()
    else:  # Jeśli jest to pierwsze wyświetlenie strony
        return None, None


@main_panel_blueprint.route('/', methods=['GET', 'POST'])
def main_panel():
    album = None
    results = None
    return render_template('main-panel.html', album=album, results=results)


@main_panel_blueprint.route('/album-generator', methods=['GET', 'POST'])
def album_generator():
    album, results = process_album_request()
    return render_template('album-generator.html', album=album, results=results)


@main_panel_blueprint.route('/about')
def about():
    return render_template('about.html')


@main_panel_blueprint.route('/links')
def links():
    return render_template('links.html')