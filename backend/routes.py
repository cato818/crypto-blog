from flask import Blueprint, request, jsonify
from models import User, Prediction
from database import db_session

routes = Blueprint('routes', __name__)

@routes.route('/api/predictions', methods=['GET'])
def get_predictions():
    predictions = Prediction.query.all()
    return jsonify([prediction.to_dict() for prediction in predictions])

@routes.route('/api/subscribe', methods=['POST'])
def subscribe_user():
    data = request.json
    new_user = User(email=data['email'])
    db_session.add(new_user)
    db_session.commit()
    return jsonify({'message': 'Subscription successful!'}), 201

@routes.route('/api/reset', methods=['POST'])
def reset_data():
    db_session.query(Prediction).delete()
    db_session.commit()
    return jsonify({'message': 'Daily data reset successful!'}), 200