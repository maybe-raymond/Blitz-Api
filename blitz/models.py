from blitz import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = "Article"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    source = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False, unique=True)
    summary = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    image_src = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Article('{self.title}','{self.source}', '{self.link}', '{self.summary}')"


class Exchange_rate(db.Model):
    __tablename__ = "Exchange rate"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rtgs = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Exchange_rate('{self.rtgs}','{self.name}', '{self.date}')"


class Covid(db.Model):
    __tablename__ = "Covid"

    id = db.Column(db.Integer, primary_key=True)
    cases = db.Column(db.Integer, nullable=False)
    death = db.Column(db.Integer, nullable=False)
    recovery = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Covid('{self.cases}', '{self.death}', '{self.recovery}', '{self.date}')"
