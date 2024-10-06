from flask import Flask
from db import create_app
from resources import api, TaskResource, AuthResource
from flask_jwt_extended import JWTManager  # Import JWTManager

app = create_app()

# Initialize JWTManager with the Flask app
jwt = JWTManager(app)

api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>', endpoint='task_resource')
api.add_resource(AuthResource, '/auth', endpoint='auth_resource')

# api.add_resource(TaskResource, '/tasks')
# api.add_resource(AuthResource, '/auth')
# api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>')  # Add <int:task_id> to capture task ID


api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
