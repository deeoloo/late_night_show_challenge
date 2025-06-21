from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

appearance_bp=Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods = ['POST'])
@jwt_required()
def appearance():
    return jsonify(message="appearance created"),201
    