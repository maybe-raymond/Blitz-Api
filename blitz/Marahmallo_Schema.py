from blitz import ma
from blitz.models import Article, Exchange_rate, Covid


class ArticleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Article
        ordered = True
    title = ma.auto_field()
    source = ma.auto_field()
    summary = ma.auto_field()
    date = ma.Date()


class CovidSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Covid
        ordered = True
    cases = ma.auto_field()
    death = ma.auto_field()
    recovery = ma.auto_field()
    active = ma.auto_field()
    date = ma.Date()


class Exchange_rateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Exchange_rate
        ordered = True
    name = ma.auto_field()
    rtgs = ma.auto_field()
    date = ma.Date()
