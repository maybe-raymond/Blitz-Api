from blitz import api, app
from blitz.tasks import Get_data
from flask_restful import Resource
from sqlalchemy import and_
from blitz.Marahmallo_Schema import ArticleSchema, CovidSchema, Exchange_rateSchema
from blitz.models import Article, Exchange_rate, Covid
from datetime import datetime


# Creating the Schema
article_schema = ArticleSchema(many=True)
covid_schema = CovidSchema()
rate_schema = Exchange_rateSchema()
all_rates_schema = Exchange_rateSchema(many=True)


class Articles(Resource):
    def get(self, name="none"):
        if (name == "none"):
            news = Article.query.order_by(Article.date.desc())
            all = article_schema.dump(news)
            return all, 200
        else:
            news = Article.query.filter_by(source=name).order_by(Article.date.desc())
            all = article_schema.dump(news)
            return all, 200


class Covid_results(Resource):
    def get(self):
        results = Covid.query.order_by(Covid.date.desc()).first()
        result = covid_schema.dump(results)
        return result, 200


class Exchange(Resource):
    def get(self, type="none"):
        t = datetime.utcnow()
        today = t.isoformat()
        if (type == "none"):
            all = Exchange_rate.query.order_by(Exchange_rate.date.desc()).limit(5).all()
            results = all_rates_schema.dump(all)
            return results, 200
        else:
            all = Exchange_rate.query.filter_by(name=type).order_by(Exchange_rate.date.desc()).first()
            result = rate_schema.dump(all)
            return result, 200


api.add_resource(Articles, "/Articles", "/Articles/<name>")
api.add_resource(Covid_results, "/Covid")
api.add_resource(Exchange, "/Exchange/<type>", "/Exchange")

@app.route("/")
def Start_up():
    Get_data()

Start_up()
