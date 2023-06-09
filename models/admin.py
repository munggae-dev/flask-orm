from services import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return (
            f"Admin('{self.id}', '{self.login_id}', '{self.password}', '{self.name}')"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "login_id": self.login_id,
            "password": self.password,
            "name": self.name,
        }
