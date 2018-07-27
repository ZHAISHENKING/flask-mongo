from flask import Flask


def create_app(app_name="HOMEWORK_API"):
    app = Flask(app_name)
    app.config.from_object('v1.config')
    # 初始化app
    return app