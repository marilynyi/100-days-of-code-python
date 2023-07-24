import csv
import config
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config["SECRET_KEY"] = config.secret_key
Bootstrap5(app)

class CafeForm(FlaskForm):
    """Creates a form to add a new cafe entry.

    Args:
        cafe (str): Name of the cafe
        location (str): Google Maps location of cafe; include http
        open (str): business open time e.g. 8AM
        close (str): business closing time e.g. 5:30PM
        coffee_rating (select str): coffee rating from 1 (worst) to 5 (best)
        wifi_rating (select str): wifi rating from 1 (worst) to 5 (best)
        power_rating (select str): power rating from X (not available) to 5 (best)
    """
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", 
                                choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength",
                              choices=["🛜","🛜🛜","🛜🛜🛜","🛜🛜🛜🛜","🛜🛜🛜🛜🛜"],
                              validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", 
                               choices=["❌","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    # Set default ratings to 4
    form = CafeForm(coffee_rating="☕️☕️☕️☕️", wifi_rating="🛜🛜🛜🛜", power_rating="🔌🔌🔌🔌")
    if form.validate_on_submit():
        # Standardize time inputs into #:##AM/PM format
        form.open.data = form.open.data.replace(" ", "").replace(".", "").upper()
        form.close.data = form.close.data.replace(" ", "").replace(".", "").upper()
        # Add new cafe entry to csv
        with open('cafe-data.csv', mode='a') as csv_file:
            # Commas go inside each string so csv can delineate properly
            csv_file.write(f"\n{form.cafe.data},"
                       f"{form.location.data},"
                       f"{form.open.data},"
                       f"{form.close.data},"
                       f"{form.coffee_rating.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.power_rating.data}"                       
                       )
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    # Read CSV data and create list of rows
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
