'''
simple flask app with db
date: 5/25/2020
author: Mikele
email: wei40680@protonmail.com
'''
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
DB_URL = 'sqlite:///test.sqlite'
# mysql+{driver}://{username}:{password}@{hostname}:{port}/dbname
# or mysql://...
# DB_URL = 'mysql+pymysql://user:password@localhost:3306/flaskbase'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)


class Item(db.Model):
    '''Model'''
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(500))
    dimension = db.Column(db.Float)
    weblink = db.Column(db.String(200))
    descrition = db.Column(db.String(10000))

    def __str__(self):
        return '<Item % >' % self.about


db.create_all()


@app.route('/')
def index():
    '''Home page read item from db'''
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 100, type=int)
    pagination = Item.query.paginate(page, per_page=limit)
    items = pagination.items
    total = Item.query.count()
    return render_template('index.html', items=items, pages=pagination)


@app.route('/<item_id>')
def item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    if item:
        return render_template('item.html', item=item)
    return 'Page not found <a href="/">go back home page</a>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
