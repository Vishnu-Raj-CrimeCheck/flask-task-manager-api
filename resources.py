from flask_restful import Resource, Api,reqparse
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from models import Task
from db import db

api = Api()

class AuthResource(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        # Here you would verify username and password
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}

class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=False, help='Title of the task')
    parser.add_argument('description', type=str, required=False, help='Description of the task')
    parser.add_argument('completed', type=bool, required=False, help='Task completion status')

    @jwt_required()  # Require JWT token for accessing this endpoint
    def get(self, task_id=None):
        # If task_id is provided, return a specific task
        if task_id:
            task = Task.query.get(task_id)
            if not task:
                return {'message': 'Task not found'}, 404
            return task.to_dict(), 200

        # If task_id is not provided, return all tasks
        tasks = Task.query.all()
        return [task.to_dict() for task in tasks], 200

    @jwt_required()
    def put(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404

        data = TaskResource.parser.parse_args()
        if data['title']:
            task.title = data['title']
        if data['description']:
            task.description = data['description']
        if data['completed'] is not None:
            task.completed = data['completed']

        db.session.commit()
        return {'message': 'Task updated successfully', 'task': task.to_dict()}, 200
