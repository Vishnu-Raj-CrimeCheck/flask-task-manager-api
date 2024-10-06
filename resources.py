from flask_restful import Resource, Api,reqparse

from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from models import Task
from db import db
# from flask_restful import Resource, reqparse
# from models import Task
# from flask import request
# from db import db
# from flask_jwt_extended import jwt_required

api = Api()

# class TaskResource(Resource):
#     def get(self):
#         tasks = Task.query.all()
#         return [{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks]

#     @jwt_required()
#     def post(self):
#         data = request.get_json()
#         new_task = Task(title=data['title'], description=data.get('description'))
#         db.session.add(new_task)
#         db.session.commit()
#         return {'id': new_task.id}, 201

class AuthResource(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        # Here you would verify username and password
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}




# class TaskResource(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('title', type=str, required=False, help='Title of the task')
#     parser.add_argument('description', type=str, required=False, help='Description of the task')
#     parser.add_argument('completed', type=bool, required=False, help='Task completion status')

#     @jwt_required()  # Require JWT token for accessing this endpoint
#     def put(self, task_id):
#         # Find the task by its ID
#         task = Task.query.get(task_id)
#         if not task:
#             return {'message': 'Task not found'}, 404

#         # Parse the request body for updates
#         data = TaskResource.parser.parse_args()

#         # Update the task details if provided
#         if data['title']:
#             task.title = data['title']
#         if data['description']:
#             task.description = data['description']
#         if data['completed'] is not None:  # Check if 'completed' status is provided
#             task.completed = data['completed']

#         # Save the changes to the database
#         db.session.commit()

#         return {'message': 'Task updated successfully', 'task': task.to_dict()}, 200


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
