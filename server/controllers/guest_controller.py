from flask import Blueprint, jsonify

guest_bp= Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def guests():
    return jsonify(message="Public guests list")