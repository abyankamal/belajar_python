from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
db = SQLAlchemy(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["1", "2", "3", "4", "5"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    submit = SubmitField('Submit')

class Cafe(db.Model):
    __tablename__ = 'cafes'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    cafe: Mapped[str] = mapped_column(db.String(80), nullable=False)
    location: Mapped[str] = mapped_column(db.String(200), nullable=False)
    open: Mapped[str] = mapped_column(db.String(20), nullable=False)
    close: Mapped[str] = mapped_column(db.String(20), nullable=False)
    coffee_rating: Mapped[float] = mapped_column(Float, nullable=False)
    wifi_rating: Mapped[float] = mapped_column(Float, nullable=False)
    power_rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            cafe=form.cafe.data,
            location=form.location.data,
            open=form.open.data,
            close=form.close.data,
            coffee_rating=float(form.coffee_rating.data),
            wifi_rating=float(form.wifi_rating.data),
            power_rating=float(form.power_rating.data)
        )
        db.session.add(new_cafe)
        db.session.commit()
        return "Cafe added successfully!"
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Cafe).order_by(Cafe.cafe))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_cafes = result.scalars().all()
    return render_template("cafes.html", cafes=all_cafes)

@app.route('/edit/<int:cafe_id>', methods=['GET', 'POST'])
def edit_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    form = CafeForm(obj=cafe)
    if form.validate_on_submit():
        cafe.cafe = form.cafe.data
        cafe.location = form.location.data
        cafe.open = form.open.data
        cafe.close = form.close.data
        cafe.coffee_rating = float(form.coffee_rating.data)
        cafe.wifi_rating = float(form.wifi_rating.data)
        cafe.power_rating = float(form.power_rating.data)
        db.session.commit()
        return redirect(url_for('show_cafes'))
    return render_template('edit_cafe.html', form=form, cafe_id=cafe.id)

@app.route('/delete/<int:cafe_id>', methods=['POST'])
def delete_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('show_cafes'))

if __name__ == '__main__':
    app.run(debug=True)
