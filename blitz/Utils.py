from blitz.models import Article
from datetime import datetime


def check(s):
    data = Article.query.filter_by(source=s).all()
    return data


def all_check(model, source):
    t = datetime.utcnow()
    today = t.isoformat()
    if source != "zimrates":
        p = model.query.order_by(model.date.desc()).first()
        n = p.date.isoformat()
        if (today.split("T")[0] != n.split("T")[0]):
            return True
    else:
        p = model.query.filter_by(name=source).order_by(model.date.desc()).first()
        n = p.date.isoformat()
        if (today.split("T")[0] != n.split("T")[0]):
            return True
