import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import main_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)