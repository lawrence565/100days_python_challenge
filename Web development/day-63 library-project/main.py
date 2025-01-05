from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
bootstrap = Bootstrap5(app)

class BookForm(FlaskForm):
    book = StringField('Book', validators=[DataRequired()])
    arthur = StringField('Arthur', validators=[DataRequired()])
    rating = SelectField(label='Rating',
                                      choices=[(0, 'No Star'), (1, '⭐'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (5, '⭐️⭐️⭐️⭐️⭐️')],
                                      validators=[DataRequired()])
    submit = SubmitField('Submit')

# SQLAlchemy Application
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)

with app.app_context():
    db.create_all()

# Flask Application
@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()

    if request.method == 'POST' and form.validate_on_submit():

        book = Book(
            title=form.book.data,
            author=form.arthur.data,
            rating=form.rating.data
        )
        db.session.add(book)
        db.session.commit()

        return redirect('/')

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run()

