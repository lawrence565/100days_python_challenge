from flask import Flask, render_template, request, redirect
from emailNotification import sending_email
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog/<_id>")
def blog(_id):
    for post in posts:
        if str(post['id']) == _id:
            return render_template('post.html', post=post)
    else:
        return render_template("index.html", all_posts=posts)

@app.route("/form", methods=['POST'])
def receive_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    sending_email(name, email, phone, message)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)