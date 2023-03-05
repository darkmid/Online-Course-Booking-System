from flask_restx import Namespace,Resource
from datetime import datetime

api = Namespace("health")

@api.route("/")
class HealthApi(Resource):
    def get(self):
        return [{"status":"up","datetime iso":datetime.utcnow().isoformat(),"datetime str":str(datetime.utcnow())}]
    
@api.route("/deepcheck")
class HealthApi(Resource):
    def get(self):
        return [{"status":"up"}]
    
