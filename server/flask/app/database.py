from app import app
from flask_sqlalchemy import SQLAlchemy
import os
import time

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'postgres'

DB = SQLAlchemy(app)

from app.models import SampleTable

# function to insert/update an object in the DB
def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            DB.session.commit()
            return True
        except SQLAlchemyError as e:
            DB.session.rollback()
            return False
        finally:
            DB.session.close()
    return persist


@db_persist
def insert_or_update(table_object):
    return DB.session.merge(table_object)


dbstatus = False
while dbstatus is False:
    try:
        DB.create_all()
        DB.session.commit()
    except Exception as e:
        time.sleep(2)
    else:
        dbstatus = True
