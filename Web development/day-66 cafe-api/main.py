import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    results = db.session.query(Cafe).all()
    cafe = random.choice(results)
    return jsonify(cafe={
        'id': cafe.id,
        'name': cafe.name,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'seats': cafe.seats,
        'amenities': {
            'has_toilet': cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'has_sockets': cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
        },
        'coffee_price': cafe.coffee_price,
    })


@app.route("/all")
def all_cafes():
    results = db.session.query(Cafe).all()
    cafes = []
    for result in results:
        cafe = {result.name: {
            'id': result.id,
            'name': result.name,
            'map_url': result.map_url,
            'img_url': result.img_url,
            'location': result.location,
            'seats': result.seats,
            'amenities': {
                'has_toilet': result.has_toilet,
                'has_wifi': result.has_wifi,
                'has_sockets': result.has_sockets,
                'can_take_calls': result.can_take_calls,
            },
            'coffee_price': result.coffee_price,
        }}
        cafes.append(cafe)
    print(cafes)

    return jsonify(cafes)


@app.route('/search')
def search_area():
    area = request.args.get('loc')
    name = request.args.get('name')
    cafes = []
    if area:
        results = db.session.query(Cafe).filter(Cafe.location == area.title()).all()
    elif name:
        results = db.session.query(Cafe).filter(Cafe.name == name.title()).all()
    else:
        results = []

    if len(results) == 0:
        return jsonify({'error': {
            'Not Found': 'Sorry, we do not have cafe in that location.'
        }})
    else:
        for result in results:
            cafe = {result.name: {
                'id': result.id,
                'name': result.name,
                'map_url': result.map_url,
                'img_url': result.img_url,
                'location': result.location,
                'seats': result.seats,
                'amenities': {
                    'has_toilet': result.has_toilet,
                    'has_wifi': result.has_wifi,
                    'has_sockets': result.has_sockets,
                    'can_take_calls': result.can_take_calls,
                },
                'coffee_price': result.coffee_price,
            }}
            cafes.append(cafe)

        return jsonify(cafes)


# HTTP POST - Create Record
@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        if request.form.get('has_toilet') == 'true':
            toilet = True
        else:
            toilet = False
        if request.form.get('has_wifi') == 'true':
            wifi = True
        else:
            wifi = False
        if request.form.get('has_sockets') == 'true':
            socket = True
        else:
            socket = False
        if request.form.get('can_take_calls') == 'true':
            calls = True
        else:
            calls = False

        cafe = Cafe(
            name=request.form.get('name'),
            map_url=request.form.get('map_url'),
            img_url=request.form.get('img_url'),
            location=request.form.get('location'),
            seats=request.form.get('seats'),
            has_toilet=toilet,
            has_wifi=wifi,
            has_sockets=socket,
            can_take_calls=calls,
            coffee_price='NT$' + request.form.get('coffee_price')
        )
        db.session.add(cafe)
        db.session.commit()

        return jsonify({'response': {
            'Success': 'Successfully add coffee shop'
        }}), 200

    return render_template('add_cafe.html')


# HTTP PUT/PATCH - Update Record
@app.route('/update_price/<_id>', methods=['patch'])
def update_price(_id):
    new_price = request.args.get('price')

    cafe = db.session.query(Cafe).filter(Cafe.id == _id).first()
    if not cafe:
        return jsonify({
            'error': {
                'Not Found': 'Sorry a cafe with the id is not found in the database.'
            }}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify({
            'success': 'Successfully update the price.'
        }), 200


# HTTP DELETE - Delete Record
@app.route('/report_closed/<_id>', methods=['DELETE'])
def update_price(_id):
    api_key = request.args.get('api_key')
    if api_key != 'delete_cafe':
        return jsonify({
            'error': {
                'Api Key Error': "Sorry, that's not allowed. Make sure you have the right api_key."
            }}), 404

    cafe = db.session.query(Cafe).filter(Cafe.id == _id).first()
    if not cafe:
        return jsonify({'error': {
            'Not Found': 'Sorry a cafe with the id is not found in the database.'
        }}), 404
    db.session.delete(Cafe).filter(Cafe.id == _id).first()
    return jsonify({
        'success': 'Successfully report the Cafe closed.'
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
