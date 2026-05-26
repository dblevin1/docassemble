import datetime
from docassemble.base.config import daconfig
from docassemble.webapp.core.models import JsonStorage as CoreJsonStorage
import docassemble.webapp.db_object
from sqlalchemy import false, delete, select, func
from sqlalchemy.dialects.postgresql.json import JSONB

custom_db = daconfig.get('variables snapshot db', None)
db = docassemble.webapp.db_object.db

if custom_db is None:
    JsonStorage = CoreJsonStorage

    def variables_snapshot_connection():
        return db.engine.raw_connection()

    def variables_snapshot_connect():
        return db.engine.connect()
else:
    import docassemble.webapp.user_database  # pylint: disable=ungrouped-imports
    _snapshot_url = docassemble.webapp.user_database.alchemy_url('variables snapshot db')

    class JsonStorage(db.Model):
        __tablename__ = "jsonstorage"
        __bind_key__ = 'variables_snapshot'
        id = db.Column(db.Integer(), primary_key=True)
        filename = db.Column(db.String(255), index=True)
        key = db.Column(db.String(250), index=True)
        if _snapshot_url.startswith('postgresql'):
            data = db.Column(JSONB)
        else:
            data = db.Column(db.Text())
        tags = db.Column(db.Text())
        modtime = db.Column(db.DateTime(), server_default=func.now())  # pylint: disable=not-callable
        persistent = db.Column(db.Boolean(), nullable=False, server_default=false())

    from docassemble.webapp.app_object import app
    with app.app_context():
        db.create_all(bind_key='variables_snapshot')

    def variables_snapshot_connection():
        return db.engines['variables_snapshot'].raw_connection()

    def variables_snapshot_connect():
        return db.engines['variables_snapshot'].connect()


def read_answer_json(user_code, filename, tags=None, all_tags=False):
    if all_tags:
        entries = []
        for entry in db.session.execute(select(JsonStorage).filter_by(filename=filename, key=user_code, tags=tags)).scalars():
            entries.append({'data': entry.data, 'tags': entry.tags, 'modtime': entry.modtime})
        return entries
    existing_entry = db.session.execute(select(JsonStorage).filter_by(filename=filename, key=user_code, tags=tags)).scalar()
    if existing_entry is not None:
        return existing_entry.data
    return None


def write_answer_json(user_code, filename, data, tags=None, persistent=False):
    existing_entry = db.session.execute(select(JsonStorage).filter_by(filename=filename, key=user_code, tags=tags).with_for_update()).scalar()
    if existing_entry:
        existing_entry.data = data
        existing_entry.modtime = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        existing_entry.persistent = persistent
    else:
        new_entry = JsonStorage(filename=filename, key=user_code, data=data, tags=tags, persistent=persistent, modtime=datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None))
        db.session.add(new_entry)
    db.session.commit()


def delete_answer_json(user_code, filename, tags=None, delete_all=False, delete_persistent=False):
    if delete_all:
        if delete_persistent:
            db.session.execute(delete(JsonStorage).filter_by(filename=filename, key=user_code))
        else:
            db.session.execute(delete(JsonStorage).filter_by(filename=filename, key=user_code, persistent=False))
    else:
        db.session.execute(delete(JsonStorage).filter_by(filename=filename, key=user_code, tags=tags))
    db.session.commit()
