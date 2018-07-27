from flask import Flask
from flask_cors import CORS
from routes import api, rc


def create_app(app_name='HOMEWORK_API'):
    app = Flask(app_name)
    app.config.from_object('v1.config')
    api.init_app(app)

    app.register_blueprint(rc)
    CORS(app, supports_credentials=True)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # 初始化app
    return app