def commit(db):
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def rollback(db):
    try:
        db.session.rollback()
    except Exception as e:
        raise e


def add(db, data):
    db.session.add(data)


def delete(db, data):
    db.session.delete(data)


def select_all(db, model):
    return model.query.all()


def update(db, origin, update: dict):
    for k, v in update.items():
        if k == "id":
            # id는 변경 불가
            continue
        setattr(origin, k, v)
    return origin


#  test zone
# from models import admin

# origin = admin.Admin(
#     id=1,
#     login_id="test",
#     password="pw1234",
#     name="admin"
# )

# updater = {
#     "login_id": "test2",
#     "password": "pw12345",
#     "name": "admin2"
# }

# update("", origin, updater)
