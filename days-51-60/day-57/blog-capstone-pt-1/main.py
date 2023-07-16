import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    return render_template("post.html", posts=all_posts, id=blog_id)
    
if __name__ == "__main__":
    app.run(debug=True)
