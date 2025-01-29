from VC_Radio_app import create_app

VC_Radio_app = create_app()

if __name__ == "__main__":
    VC_Radio_app.run(debug=True, port=5000)
