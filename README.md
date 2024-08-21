# Django CRUD API Project

This repository contains a basic Django project that demonstrates CRUD (Create, Read, Update, Delete) operations using the Django REST Framework. The project is designed to help beginners understand how to build RESTful APIs in Django.

## Project Structure

The project is divided into two main apps:

1. **Drinks** (Main App): Manages the `Drink` model, which includes CRUD operations.
2. **Foods**: Manages the `Food` model, which also includes CRUD operations.

## What is a REST API?

A REST (Representational State Transfer) API is a way to build web services that interact with resources. It uses standard HTTP methods like GET, POST, PUT, and DELETE to perform CRUD operations. REST APIs are stateless and rely on URIs (Uniform Resource Identifiers) to access resources.

### Key Characteristics of REST APIs:
- **Stateless**: Each request from a client to a server must contain all the information needed to understand and process the request.
- **Uniform Interface**: Resources are identified in requests (usually as URLs), and interactions with these resources are performed using standard HTTP methods.
- **Client-Server Architecture**: The client and server are separate, allowing for independent development and scaling.
- **Layered System**: REST APIs can use layers, such as security or caching layers, without the client being aware of them.

## HTTP Status Codes

- **200 OK**: The request was successful.
- **201 Created**: A new resource has been successfully created.
- **204 No Content**: The request was successful, but there's no content to return (often used after a DELETE operation).
- **400 Bad Request**: The server could not understand the request due to invalid syntax.
- **404 Not Found**: The requested resource could not be found on the server.
- **500 Internal Server Error**: The server encountered an unexpected condition that prevented it from fulfilling the request.

## Project Setup

### Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MuhammedBasith/django-crud-api.git
   cd django-crud-api
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

### API Endpoints

#### Drinks API

- **GET /drinks/**: Retrieve a list of all drinks.
- **POST /drinks/**: Create a new drink.
- **GET /drinks/<int:id>/**: Retrieve a specific drink by its ID.
- **PUT /drinks/<int:id>/**: Update a specific drink by its ID.
- **DELETE /drinks/<int:id>/**: Delete a specific drink by its ID.

#### Foods API

- **GET /foods/**: Retrieve a list of all foods.

### Example Requests

1. **Get all drinks**:

   ```bash
   curl -X GET http://127.0.0.1:8000/drinks/
   ```

2. **Create a new drink**:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "Coca Cola", "description": "A refreshing soft drink"}' http://127.0.0.1:8000/drinks/
   ```

3. **Get a specific drink**:

   ```bash
   curl -X GET http://127.0.0.1:8000/drinks/1/
   ```

4. **Update a specific drink**:

   ```bash
   curl -X PUT -H "Content-Type: application/json" -d '{"name": "Pepsi", "description": "Another refreshing soft drink"}' http://127.0.0.1:8000/drinks/1/
   ```

5. **Delete a specific drink**:

   ```bash
   curl -X DELETE http://127.0.0.1:8000/drinks/1/
   ```


## Running Tests

### Unit Tests with `pytest`

This project includes unit tests for the `Drink` model and its corresponding views using `pytest` and `pytest-django`. These tests cover the basic CRUD operations.

### Prerequisites

- `pytest`
- `pytest-django`

### Setup

Ensure that `pytest` and `pytest-django` are installed:

```bash
pip install pytest pytest-django
```

### Running Tests

To run the tests, simply execute:

```bash
pytest
```

This will run all the unit tests in the project and provide detailed output on test results.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
