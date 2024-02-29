from VC_Radio_app import create_app
from VC_Radio_app.views.main_panel import main_panel_blueprint


VC_Radio_app = create_app()
VC_Radio_app.register_blueprint(main_panel_blueprint)

if __name__ == "__main__":
    VC_Radio_app.run(debug=True, port=5000)
