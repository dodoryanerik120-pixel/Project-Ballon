from app import db
from sqlalchemy import text

def sql(req):
    result = db.session.execute(text(req))
    return [dict(row) for row in result.mappings().all()]