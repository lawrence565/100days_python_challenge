from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField(label='Open Time, e.g. 8A.M.', validators=[DataRequired()])
    close_time = StringField(label='Closing Time, e.g. 9A.M.', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating',
                                choices=[(0, '✘'), (1, '☕'), (2, '☕☕'), (3, '☕☕☕'), (4, '☕☕☕☕'), (5, '☕☕☕☕☕')],
                                validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Rating',
                              choices=[(0, '✘'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')],
                              validators=[DataRequired()])
    power_outlet_rating = SelectField(label='Power Outlet Rating',
                                      choices=[(0, '✘'), (1, '🔌'), (2, '🔌🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')],
                                      validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if request.method == 'POST':
        if form.validate_on_submit():
            with open('cafe-data.csv', newline='', encoding='utf-8', mode='w') as csv_file:
                csv_data = csv.writer(csv_file, delimiter=',')
                csv_data.writerow([form.cafe.data, form.location_url.data, form.open_time.data, form.close_time.data,
                                   form.coffee_rating.data, form.wifi_rating.data, form.power_outlet_rating.data])

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run()
