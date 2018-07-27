from v1.api_1_0 import *
from flask import Blueprint
from flask_restful import Api

api = Api()
rc = Blueprint('rc', __name__)

api.add_resource(Index,'/', endpoint='home')
api.add_resource(ServerFile, '/f/<id>', endpoint='serverfile')
api.add_resource(UploadAPI, '/upload/', endpoint='upload')
api.add_resource(HomeworkInfoAPI, '/student_all/<id>/', endpoint='hemoinfo')