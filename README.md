# 💰 Financial Analytics Backend System

A Django-based backend system for managing and analyzing financial transactions with role-based access control, filtering, and analytics capabilities.

---

## 🚀 Overview

This project is a modular and scalable backend system designed to handle financial records such as income and expenses. It provides REST APIs for transaction management and analytical insights, making it suitable for powering a finance dashboard or SaaS application.

---

## 🧠 Key Features

### 🔹 Transaction Management
- Create, read, update, and delete financial records
- Fields include amount, type (income/expense), category, date, and notes
- User-specific data isolation

### 🔹 Filtering & Pagination
- Filter transactions by:
  - Type
  - Category
  - Date range
- Built-in pagination using Django REST Framework

### 🔹 Analytics Engine
- Total income
- Total expenses
- Current balance
- Category-wise expense breakdown
- Aggregation using Django ORM

### 🔹 Role-Based Access Control
- **Viewer** → Read-only access
- **Analyst** → Access to analytics and filtered data
- **Admin** → Full CRUD access

### 🔹 API Documentation
- Interactive Swagger UI for testing APIs

### 🔹 Database
- PostgreSQL used for reliable and scalable data storage

### 🔹 Unit Testing
- Basic test cases implemented for core functionality

---

## 🏗️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **API Docs:** drf-yasg (Swagger)  
- **Filtering:** django-filter  

---

## 📂 Project Structure



---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Vedukharatmal/Finance-System-Backend.git
cd finance-system

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```
## configure postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finance_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


```bash 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Documentation available at
http://127.0.0.1:8000/swagger/


## RUN TESTS
python manage.py test
