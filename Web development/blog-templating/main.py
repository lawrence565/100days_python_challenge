from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", all_blog=post_objects)

@app.route("/blog/<int:id>")
def get_blog(id):
    requests_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            requests_post =blog_post

    return render_template('post.html', blog=requests_post)

if __name__ == "__main__":
    app.run(debug=True)
