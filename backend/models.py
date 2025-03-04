from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscribed_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(50), nullable=False)
    predicted_price = db.Column(db.Float, nullable=False)
    prediction_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Prediction {self.currency} - {self.predicted_price}>'