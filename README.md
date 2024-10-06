# Flask Task Manager API

## Overview

The **Flask Task Manager API** is a simple and scalable task management API built using the Flask web framework. It allows users to create, retrieve, and update tasks. The API is secured using **JWT (JSON Web Token)** authentication, ensuring that only authenticated users can manage tasks. The project uses **Flask-RESTful** for building the API and **SQLAlchemy** as the ORM for database management.

---

## Features

- **Task CRUD Operations**: Create, Read, and Update tasks (Delete can be added later).
- **JWT Authentication**: Secure the API endpoints using token-based authentication.
- **Modular Structure**: Scalable with Flask Blueprints.
- **Database Support**: Uses SQLAlchemy with SQLite (can switch to PostgreSQL for production).
- **Token-based Authorization**: Only authenticated users can access the API.
- **Task Completion Status**: Mark tasks as completed.

---

## Technologies Used

- **Flask**: Web framework.
- **Flask-RESTful**: For building RESTful APIs.
- **Flask-JWT-Extended**: For handling JWT-based authentication.
- **SQLAlchemy**: ORM for database interactions.
- **Flask-Migrate**: For handling database migrations.
- **SQLite**: Database (can be swapped with PostgreSQL).
- **Gunicorn**: WSGI server for deployment.

---

## Endpoints

### 1. **Authentication**

#### Login (POST `/auth`)
Authenticate a user and return a JWT token.

- **Request**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }

- **Response**:
  ```json
  {  
    "access_token": "your_jwt_token"
  }



### 2. **Tasks**

#### Create a Task (POST `/tasks`)
Create a new task.

- **Request**:
  ```json
    {
    "title": "Task title",
    "description": "Task description"
    }

- **Response**:
  ```json
    {
      "id": 1,
      "title": "Task title",
      "description": "Task description",
      "completed": false
    }



#### Retrieve All Tasks (GET `/tasks`)

- **Response**:
  ```json
    [
      {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Bread, Eggs",
        "completed": false
      },
      {
        "id": 2,
        "title": "Clean the house",
        "description": "Vacuum and mop",
        "completed": true
      }
    ]

    ]

#### Retrieve a Single Task (GET `/tasks/<task_id>`)

- **Response**:
  ```json
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, Bread, Eggs",
      "completed": false
    }


  