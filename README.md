# FLASK ORM EXAMPLE
writed by MungGae

# 1. Setup
## 1-1 Create venv enviroment
```bash
# ubuntu 22.04 
python3 -m venv venv

# actiavate
source venv/bin/activate

```

## 1-2 Install dependency

```bash
pip install -r requirements.txt
```

or 

```bash 
pip install flask flask_cors flask-migrate python-dotenv pymysql
```

### requirements.txt
```txt
alembic==1.11.1
blinker==1.6.2
click==8.1.3
Flask==2.3.2
Flask-Cors==3.0.10
Flask-Migrate==4.0.4
Flask-SQLAlchemy==3.0.3
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
Mako==1.2.4
MarkupSafe==2.1.3
PyMySQL==1.0.3
python-dotenv==1.0.0
six==1.16.0
SQLAlchemy==2.0.15
typing_extensions==4.6.3
Werkzeug==2.3.6
```

## 1-3 .env and config

.env
```.env
# MYSQL DB PARAMETER
DB_USER=
DB_PW=
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=
```

config.py

```python
from dotenv import dotenv_values
import os

BASE_DIR = os.path.dirname(__file__)

config = dotenv_values(".env")

#mysql
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config["DB_USER"]}:{config["DB_PW"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}?charset=utf8'

# sqlite
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'test.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

# 2. DB setup
Use flask-migrate [#](https://flask-migrate.readthedocs.io/en/latest/)


## 2-1 DB init

```bash
flask db init
flask db migrate
flask db upgrade
```

## DB UPDATE

```bash
flask db migrate
flask db upgrade
```


# 3. Debug Running
```bash
python app.py
```