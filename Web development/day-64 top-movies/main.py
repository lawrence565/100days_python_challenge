from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import requests

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
IMG_ADDRESS = 'https://image.tmdb.org/t/p/w500'
Bootstrap5(app)


class AddMovieForm(FlaskForm):
    title = StringField('Movie', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RateMovieForm(FlaskForm):
    rating = SelectField(label='Your Rating out of five',
                         choices=[(0, 'No Star'), (1, '⭐'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'),
                                  (5, '⭐️⭐️⭐️⭐️⭐️')],
                         validators=[DataRequired()])
    # ranking = StringField('Ranking (1-10)', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()

    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        header = {
            "accept": "application/json",
            "Authorization": "Bearer " + ACCESS_TOKEN,
        }
        params = {
            'query': title,
        }
        res = requests.get('https://api.themoviedb.org/3/search/movie', params=params, headers=header)
        return render_template('select.html', movies=res.json()['results'])
    return render_template('add.html', form=form)


@app.route("/select", methods=['GET'])
def select_movie():
    _id = request.args.get("id")

    header = {
        "accept": "application/json",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }

    res = requests.get('https://api.themoviedb.org/3/movie/' + _id, headers=header)
    movie = res.json()

    print(movie, 'success')
    new_movie = Movie(
        title=movie["title"],
        year=movie['release_date'][:4],
        description=movie["overview"],
        img_url=IMG_ADDRESS + movie["poster_path"],
    )
    db.session.add(new_movie)
    db.session.commit()

    new_id = db.session.query(Movie).filter(Movie.title == movie['title']).first().id

    return redirect(url_for('rate_movie', id = new_id))


@app.route("/rate", methods=['GET', 'POST'])
def rate_movie():
    _id = request.args.get("id")

    movie = db.session.execute(db.select(Movie).where(Movie.id == _id)).scalar()
    form = RateMovieForm(obj=movie)

    if request.method == 'POST' and form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect("/")

    return render_template('edit.html', form=form)


@app.route("/update/<_id>", methods=['GET', 'POST'])
def update_movie(_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == _id)).scalar()
    form = RateMovieForm(obj=movie)

    if request.method == 'POST' and form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()  # 提交更改
        return redirect("/")

    return render_template('edit.html', form=form)


@app.route("/delete/<_id>", methods=['GET'])
def delete_movie(_id):
    db.session.execute(db.delete(Movie).where(Movie.id == _id))
    db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
