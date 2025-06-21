from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from server.models.user import User
from server.app import db


auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data=request.get_json()
    user=User(username=data['username'])
    user.passwrord_hash=generate_password_hash(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered"), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    user=User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['Password']):
        token=create_access_token(identity=user.id)
        return jsonify(access_token=token)
    return jsonify(message="Invalid Credentials"), 401
