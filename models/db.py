from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
migrate = Migrate()


class BaseModel(DB.Model):
    __abstract__ = True

    def __repr__(self):
        return f"{self.__class__.__name__} : {self.to_dict()}"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
if __name__ == "main":
    a = BaseModel()
    a.to_dict()
