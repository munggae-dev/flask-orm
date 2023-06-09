from dotenv import dotenv_values
import os

BASE_DIR = os.path.dirname(__file__)

config = dotenv_values(".env")

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config["DB_USER"]}:{config["DB_PW"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}?charset=utf8'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
