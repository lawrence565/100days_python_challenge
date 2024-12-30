from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = 'A_secret_key'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            print(login_form.email.data)
            print(login_form.password.data)
            return redirect('/success')
    return render_template('login.html', form=login_form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run()
