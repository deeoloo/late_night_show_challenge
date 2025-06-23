from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.app import db


appearance_bp=Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    from server.models.appearance import Appearance
    data = request.get_json()
    try:
        new_appearance = Appearance(
            guest_id=data['guest_id'],
            episode_id=data['episode_id'],
            rating=data['rating']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except KeyError:
        return jsonify(error="guest_id, episode_id, and rating are required"), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except Exception as e:
        db.session.rollback()
        return jsonify(error="Server error"), 500

    