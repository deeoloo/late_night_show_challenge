from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.app import db 
from server.models.episode import Episode

episode_bp=Blueprint('episode', __name__)

@episode_bp.route('/episode/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify(error="Episode not found"), 404

    db.session.delete(episode)
    db.session.commit()
    return jsonify(message=f"Deleted episode {id}"), 200


@episode_bp.route('/episodes', methods=['GET'])
def episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

@episode_bp.route('/episode/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.filter_by(id=id).first()
    if not episode:
        return jsonify(error="Episode not found"), 404
    return jsonify(episode.to_dict()), 200


