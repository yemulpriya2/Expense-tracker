Expense Tracker API

Overview

Expense Tracker API is a Django REST Framework application that helps users track their daily expenses, monitor spending habits, and generate financial summaries.

The system provides secure JWT authentication and allows users to create, update, delete, and view their expenses while ensuring that users can only access their own data.

Problem Statement

Many people track expenses using notebooks, Excel sheets, or mobile notes, which often leads to:

Missing expense records
Difficulty calculating monthly spending
No category-wise expense analysis
Poor financial planning
This API solves these problems by providing a centralized expense management system.

Features

Authentication

JWT Login
JWT Refresh Token
Secure API Access
Expense Management

Create Expense
View Expenses
Update Expense
Delete Expense
Financial Reports

Monthly Expense Summary
Total Spending Calculation
Security

User-specific data access
Custom ownership permissions
JWT Authentication
Tech Stack

Python
Django
Django REST Framework
JWT Authentication
SQLite
Project Structure

expense_tracker/

├── manage.py

├── expense_tracker/ │ ├── settings.py │ ├── urls.py │ └── wsgi.py

└── expenses/ ├── models.py ├── serializers.py ├── views.py ├── urls.py ├── permissions.py └── admin.py

Database Design

Expense

Field| Type id| Integer user| ForeignKey title| CharField amount| DecimalField category| CharField date| DateField created_at| DateTimeField

Categories

Food Travel Shopping Bills Other

Installation

Clone Repository

git clone <repository_url>

cd expense_tracker

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Run Migrations

python manage.py makemigrations

python manage.py migrate

Create Superuser

python manage.py createsuperuser

Start Server

python manage.py runserver

Authentication

Obtain Access Token

POST

/api/token/

Request:

{ "username": "admin", "password": "admin123" }

Response:

{ "refresh": "jwt_refresh_token", "access": "jwt_access_token" }

API Endpoints

Create Expense

POST

/api/expenses/

List Expenses

GET

/api/expenses/

Retrieve Expense

GET

/api/expenses/{id}/

Update Expense

PUT

/api/expenses/{id}/

Delete Expense

DELETE

/api/expenses/{id}/

Monthly Summary

GET

/api/summary/

Example Expense Payload

{ "title": "Pizza", "amount": "500", "category": "Food", "date": "2026-06-24" }

Example Summary Response

{ "total_spent": 500 }

Testing

Postman

Generate JWT Token
Add Bearer Token in Authorization Header
Test CRUD APIs
Django Shell

python manage.py shell

Example:

from expenses.models import Expense

Expense.objects.all()

cURL

curl -X GET http://127.0.0.1:8000/api/expenses/

Key DRF Concepts Used

ModelSerializer
ModelViewSet
JWT Authentication
Custom Permissions
Aggregation Queries
ForeignKey Relationships
REST API Design
