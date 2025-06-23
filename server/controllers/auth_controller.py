from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.app import bcrypt, db 
from server.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'])
    user.password_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered"), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token),200
    return jsonify(message="Invalid Credentials"), 401