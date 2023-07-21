from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"] 
    return "<h1>Form submitted!</h1>" \
            f"<h1>Username: {username}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)