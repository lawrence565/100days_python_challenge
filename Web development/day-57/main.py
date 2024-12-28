from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)


@app.route('/')
def home():
    number = random.randint(1, 10)
    this_year = datetime.datetime.now()
    return render_template('index.html', number=number, year=this_year.year)

@app.route('/guess/<name>')
def guess(name):
    number = random.randint(1, 10)
    this_year = datetime.datetime.now()

    params = {
        'name': name
    }

    gender_res = requests.get('https://api.genderize.io', params=params)
    gender_res.raise_for_status()
    print(gender_res.json())
    gender = gender_res.json()['gender']

    age_res = requests.get('https://api.agify.io', params=params)
    age_res.raise_for_status()
    print(age_res.json())
    age = age_res.json()['age']

    return render_template('index.html', number=number, year=this_year.year, gender=gender, age=age)

@app.route("/blog")
def blog():
    res = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    res.raise_for_status()
    all_blog = res.json()

    return render_template('blog.html', all_blog=all_blog)

if __name__ == "__main__":
    app.run(debug=True)


