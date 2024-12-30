from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)