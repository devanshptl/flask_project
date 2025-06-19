#  Flask Project

This is a beginner-friendly Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a **User** resource. The application is Dockerized for easy setup and built with clean code practices.

---

## Tech Stack

- Python 3
- Flask
- MongoDB
- Flask-PyMongo
- Flask-Pydantic
- Docker & Docker Compose


---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/devanshptl/flask_project.git
cd flask_project
```

### 2. Run the app with Docker

```bash
docker-compose up --build
```

The Flask API will be available at:  
[http://localhost:5000](http://localhost:5000)

---


## Sample Request (POST)

**Endpoint:** `/users/`

```json
{
  "name": "Devansh",
  "email": "dev@example.com",
  "password": "secure123"
}
```

---

#  Testing the API

You can use the following basic curl commands to test the endpoints:

```bash
# Get all users
curl http://localhost:5000/users/

# Get a user by ID
curl http://localhost:5000/users/<id>

# Create a new user
curl -X POST http://localhost:5000/users/

# Update an existing user
curl -X PUT http://localhost:5000/users/<id>

# Delete a user
curl -X DELETE http://localhost:5000/users/<id>
```

---
