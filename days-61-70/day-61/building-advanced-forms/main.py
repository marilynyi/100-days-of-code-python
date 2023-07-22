import config
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4

# pip install Flask-WTF
# pip install wtforms[email]
# pip install bootstrap-flask

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")
    
app = Flask(__name__)
app.config["SECRET_KEY"] = config.secret_key

bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "password123":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
