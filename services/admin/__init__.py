from flask import Blueprint, request

from sqlalchemy.exc import IntegrityError

from functions import orm_helper
from services import db
from models import admin


app = Blueprint("admin", __name__, url_prefix="/admin")


@app.route("/")
def admin_root():
    return {"message": "Hello admin!"}


@app.route("/signup", methods=["POST"])
def admin_signup():
    data = request.get_json()
    try:
        login_id = data["login_id"]
    except:
        return {"message": "login_id is required"}, 400

    try:
        password = data["password"]
    except:
        return {"message": "password is required"}, 400

    try:
        name = data["name"]
    except:
        name = "foo"

    new_admin = admin.Admin(login_id=login_id, password=password, name=name)
    orm_helper.add(db, new_admin)
    try:
        orm_helper.commit(db)
    except IntegrityError as e:
        return {"message": "login_id already exist"}, 400
    except Exception as e:
        orm_helper.rollback(db)
        print(e)
        return {"message": "error"}, 500

    return {"status": 200, "message": "success", "data": new_admin.to_dict()}
