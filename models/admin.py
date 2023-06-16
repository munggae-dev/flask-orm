from models.db import BaseModel, DB


class Admin(BaseModel):
    id = DB.Column(DB.Integer, primary_key=True)
    login_id = DB.Column(DB.String(20), unique=True, nullable=False)
    password = DB.Column(DB.String(20), nullable=False)
    name = DB.Column(DB.String(20), nullable=False)

