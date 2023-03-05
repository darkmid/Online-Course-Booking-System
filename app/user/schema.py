from app.core.type import MongoModel,PydanticObjectId
from pydantic import SecretStr
from datetime import datetime

class UserSchema(MongoModel):
    id:PydanticObjectId
    username:str
    password:SecretStr
    display_name:str
    telephone:str
    campus:PydanticObjectId
    created_at:datetime

    