from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    try:
        posts = db.session.query(BlogPost).all()
    except ValueError:
        flash("There's some problem with the server!", "error")
    finally:
        return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    try:
        requested_post = db.session.query(BlogPost).filter(BlogPost.id == post_id).first()
        return render_template("post.html", post=requested_post)
    except KeyError:
        flash("There's some problem with the server!", "success")
        return redirect("/")


# TODO: add_new_post() to create a new blog post
@app.route('/add_post', methods=['GET', 'POST'])
def add_new_post():
    form = PostForm()

    if request.method == 'POST':
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date.today().strftime('%Y%m%d'),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        try:
            db.session.add(new_post)
            db.session.commit()

            flash("Post added successfully", "success")
        except ValueError:
            flash("There's some problem with the server!", "error")
        finally:
            return redirect('/')
    else:
        return render_template('make-post.html', form=form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    try:
        post = db.session.query(BlogPost).filter(BlogPost.id == post_id).first()
    except ValueError:
        return jsonify({'error': {
            'Not Found': 'The post with the id is not found.'
        }}), 404
    form = PostForm(obj=post)

    if request.method == 'POST' and form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.date = date.today()
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        db.session.commit()

        flash("Post edited successfully", "success")
        return redirect('/')
    else:
        return render_template('make-post.html', form=form)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        db.session.delete(BlogPost).filter(BlogPost.id == post_id)
        flash("Post deleted successfully", "success")
    except ValueError:
        flash("There's some problem with the server!", "error")
    finally:
        return redirect('/')


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
