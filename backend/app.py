from os import environ
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS\


DATABASE_URL = "postgres://wsiozdazunoqwa:efd187272cb7bc6b062316b9dd8eb1a1fe171ee4675ef01c03e7546f12a645f8@ec2-34-195-143-54.compute-1.amazonaws.com:5432/d659nvkdfnpq6i"
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wsiozdazunoqwa:efd187272cb7bc6b062316b9dd8eb1a1fe171ee4675ef01c03e7546f12a645f8@ec2-34-195-143-54.compute-1.amazonaws.com:5432/d659nvkdfnpq6i"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many = True)

@app.route('/', methods=['GET'])
def welcome():
    return "Hello to API"

@app.route('/get', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)


@app.route('/get/<id>/', methods=['GET'])
def post_details(id):
    article = Articles.query.get(id)
    print(article)
    return jsonify(article_schema.dump(article))


@app.route('/add', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()

    return article_schema.jsonify(articles)

@app.route('/update/<id>/', methods=['PUT'])
def update_article(id):
    article = db.session.query(Articles).get(id)
    print(article)
    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)

@app.route('/delete/<id>/', methods=['DELETE'])
def article_delete(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)
if __name__ == '__main__':
    app.run(debug=True)
