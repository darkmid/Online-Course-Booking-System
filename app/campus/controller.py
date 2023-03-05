from flask_restx import Namespace,Resource
from .model import Campus
from .schema import CampusListSchema

api = Namespace("campus")

@api.route("/")
class CampusListApi(Resource):
    def get(self):
        campus_list = list(Campus.objects())
        print(campus_list)
        return CampusListSchema.from_orm(campus_list)
