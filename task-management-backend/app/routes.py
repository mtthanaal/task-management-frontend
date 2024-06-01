from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import User, Task
from . import db

bp = Blueprint('routes', __name__)

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({'message': 'Invalid credentials'}), 401

@bp.route('/api/tasks', methods=['GET', 'POST'])
@jwt_required()
def handle_tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        return jsonify([task.as_dict() for task in tasks])
    if request.method == 'POST':
        data = request.get_json()
        new_task = Task(**data)
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.as_dict()), 201

@bp.route('/api/tasks/<int:id>', methods=['PUT', 'DELETE'])
@jwt_required()
def handle_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(task, key, value)
        db.session.commit()
        return jsonify(task.as_dict())
    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204

def init_app(app):
    app.register_blueprint(bp)
