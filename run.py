from v1.app import create_app


if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run(host='localhost', port=12341)