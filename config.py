from dotenv import dotenv_values
import os

BASE_DIR = os.path.dirname(__file__)

config = dotenv_values(".env")

# mysql
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config["DB_USER"]}:{config["DB_PW"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}?charset=utf8'

# sqlite
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'test.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
