from flask import Blueprint, render_template, request
from VC_Radio_app.utils.search_album_utils import search_album


main_panel_blueprint = Blueprint('main_panel', __name__)


@main_panel_blueprint.route('/', methods=['GET', 'POST'])
def main_panel():
    if request.method == 'POST':  # Jeśli formularz został wysłany
        album, results = search_album()
    else:  # Jeśli jest to pierwsze wyświetlenie strony
        album = None
        results = None
    return render_template('main-panel.html', album=album, results=results)


@main_panel_blueprint.route('/about')
def about():
    return render_template('about.html')


@main_panel_blueprint.route('/album-generator', methods=['GET', 'POST'])
def album_generator():
    if request.method == 'POST':  # Jeśli formularz został wysłany
        album, results = search_album()
    else:  # Jeśli jest to pierwsze wyświetlenie strony
        album = None
        results = None
    # Tutaj zwróć szablon search-album.html
    return render_template('search-album.html', album=album, results=results)