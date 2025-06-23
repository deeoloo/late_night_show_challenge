from flask import Blueprint, jsonify


guest_bp= Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def guests():
    from server.models.guest import Guest
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])