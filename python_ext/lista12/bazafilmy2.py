from flask import Flask, request, jsonify
from datetime import datetime
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String,  DateTime
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


class filmy(db.Model):
    id = Column(Integer, primary_key=True)

    tytul = Column(String, unique=False, nullable=False)

    rok = Column(Integer, unique=False, nullable=False)

    rezyser = Column(String, unique=False, nullable=False)

    operator = Column(String, unique=False, nullable=False)

    producent = Column(String, unique=False, nullable=False)

    data_dodania = Column(DateTime, default=datetime.now())

    @validates("rok")
    def validate_wykonawca(self, key, rok):
        if int(rok) > 1850:
            return rok

    def __init__(self, tytul, rok, rezyser, operator, producent):
        self.tytul = tytul
        self.rok = rok
        self.rezyser = rezyser
        self.operator = operator
        self.producent = producent


class FilmSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tytul', 'rok', 'rezyser', 'operator', 'producent')


film_schema = FilmSchema()
filmy_schema = FilmSchema(many=True)


@app.route('/filmy', methods=['POST'])
def add_film():
    tytul = request.json['tytul']
    rok = request.json['rok']
    rezyser = request.json['rezyser']
    operator = request.json['operator']
    producent = request.json['producent']

    new_film = filmy(tytul, rok, rezyser, operator, producent)

    db.session.add(new_film)
    db.session.commit()

    return film_schema.jsonify(new_film)


@app.route('/filmy', methods=['GET'])
def get_filmy():
    all_filmy = filmy.query.all()
    result = filmy_schema.dump(all_filmy)
    return jsonify(result.data)


@app.route('/filmy/<id>', methods=['GET'])
def get_film(id):
    product = filmy.query.get(id)
    return film_schema.jsonify(product)


@app.route('/filmy/<id>', methods=['PUT'])
def update_film(id):
    film = filmy.query.get(id)

    tytul = request.json['tytul']
    rok = request.json['rok']
    rezyser = request.json['rezyser']
    operator = request.json['operator']
    producent = request.json['producent']

    filmy.tytul = tytul
    filmy.rok = rok
    filmy.rezyser = rezyser
    filmy.operator = operator
    filmy.producent = producent
    db.session.commit()

    return film_schema.jsonify(film)


@app.route('/filmy/<id>', methods=['DELETE'])
def delete_film(id):
    film = filmy.query.get(id)
    db.session.delete(film)
    db.session.commit()

    return film_schema.jsonify(film)


if __name__ == '__main__':
    app.run(debug=True)
