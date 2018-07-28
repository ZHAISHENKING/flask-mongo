from v1.api_1_0 import *
from flask import Blueprint
from flask_restful import Api

api = Api()
rc = Blueprint('rc', __name__)

api.add_resource(Index,'/docs/', endpoint='home')
api.add_resource(ServerFile, '/docs/f/<id>', endpoint='serverfile')
api.add_resource(UploadAPI, '/docs/upload/', endpoint='upload')
api.add_resource(HomeworkInfoAPI, '/docs/student_all/<id>/', endpoint='hemoinfo')