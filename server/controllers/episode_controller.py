from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

episode_bp=Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods = ['DELETE'])
@jwt_required()
def delete_episode(id):
    return jsonify(message='Deleted episode{id}'),200

@episode_bp.route('/episodes', methods=['GET'])
def episodes():
    return jsonify(message="Public episodes list")

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    return jsonify(message=f"Details for episode {id} + appearances")

