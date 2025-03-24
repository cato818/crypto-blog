from flask import Blueprint, request, jsonify
from models import User, Prediction
from database import db_session

routes = Blueprint('routes', __name__)

@routes.route('/api/predictions', methods=['GET'])
def get_predictions():
    """
    Get all predictions from the database.
    :return: JSON list of predictions.
    """
    try:
        predictions = Prediction.query.all()
        return jsonify([prediction.to_dict() for prediction in predictions])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@routes.route('/api/subscribe', methods=['POST'])
def subscribe_user():
    """
    Subscribe a new user.
    :return: Success message.
    """
    data = request.json
    try:
        new_user = User(email=data['email'])
        db_session.add(new_user)
        db_session.commit()
        return jsonify({'message': 'Subscription successful!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@routes.route('/api/reset', methods=['POST'])
def reset_data():
    """
    Reset daily prediction data.
    :return: Success message.
    """
    try:
        db_session.query(Prediction).delete()
        db_session.commit()
        return jsonify({'message': 'Daily data reset successful!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500