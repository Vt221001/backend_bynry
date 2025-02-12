# Gas Utility Consumer Service API

## Overview
This is a **Django REST Framework**-based backend service for a gas utility consumer system. The system allows users to register, authenticate, create service requests, and submit feedback.

---

## Features
✅ User Registration & Authentication (Custom User Model)  
✅ Service Request Management  
✅ Feedback System  
✅ Token-based Authentication (JWT)  
✅ Secure Password Hashing  
✅ SQLite Database Support  

---

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Authentication**: JWT (JSON Web Token)

---

## Installation & Setup

### 1️⃣ Clone the Repository
```sh
 git clone <your-repo-url>
 cd Bynry_Backend/gas_utility
```

### 2️⃣ Create & Activate Virtual Environment
```sh
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations & Run Server
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Your API is now running at **http://127.0.0.1:8000/** 🎉

---

## API Endpoints

### 🔹 User Authentication

#### 1️⃣ Register User
**POST** `/api/register/`
```json
{
  "username": "testuser",
  "password": "testpassword",
  "phone": "1234567890",
  "address": "123, Street, City"
}
```

#### 2️⃣ Login & Get Token
**POST** `/api/login/`
```json
{
  "username": "testuser",
  "password": "testpassword"
}
```
_Response:_
```json
{
  "token": "your_jwt_token_here"
}
```

### 🔹 Service Requests

#### 3️⃣ Create Service Request
**POST** `/api/service-requests/`
```json
{
  "request_type": "Gas Leak",
  "details": "There is a gas leak in my kitchen."
}
```

#### 4️⃣ Get All Service Requests
**GET** `/api/service-requests/`

### 🔹 Feedback

#### 5️⃣ Submit Feedback
**POST** `/api/feedback/`
```json
{
  "service_request": 1,
  "rating": 5,
  "comment": "Excellent service!"
}
```

#### 6️⃣ Get All Feedbacks
**GET** `/api/feedback/`

---


