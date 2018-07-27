from v1.homework import *


api.add_resource(Index,'/docs/', endpoint='home')
api.add_resource(ServerFile, '/docs/f/<id>', endpoint='serverfile')
api.add_resource(UploadAPI, '/docs/upload/', endpoint='upload')
api.add_resource(HomeworkInfoAPI, '/docs/student_all/<id>/', endpoint='hemoinfo')