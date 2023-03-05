import os
from flask import Flask,Blueprint
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_restx import Api
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from .log import config_log

from app.campus.controller import api as campus_api
from app.user.controller import auth_api
from app.user import register_user_lookup
from app.core.convertor import CustomEncoder

load_dotenv("./.env")

api_bp = Blueprint("api",os.getenv("FLASK_APP_NAME"),url_prefix="/api/v1")
api = Api(api_bp)

api.add_namespace(campus_api)
api.add_namespace(auth_api)

def create_app():
    app = Flask(__name__)

    #set .env reading mode
    app.config.from_prefixed_env()
    app.config["JWT_TOKEN_LOCATION"]=["headers","cookies"]
    app.json_encoder = CustomEncoder
    app.config["RESTX_JSON"]={"cls":CustomEncoder}


    #log config
    config_log(app)

    #config MongoEngine
    MongoEngine(app)

    #JWT
    jwt=JWTManager(app)
    register_user_lookup(jwt=jwt)

    #config CORS
    CORS(app)

    #app add blueprint
    app.register_blueprint(api_bp)

    return app