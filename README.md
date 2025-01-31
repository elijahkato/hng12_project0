# HNG12 Backend Stage 0 Task 🚀

This is a simple **public API** that provides:
- 📧 **My registered email**
- 🕒 **The current UTC datetime (ISO 8601 format)**
- 🔗 **GitHub repository URL of the API source code**

## 🚀 Live API URL
[https://hng12-project0.onrender.com](https://hng12-project0.onrender.com)

---

## How to Install and Run the API Locally
Clone the repository:
Open a terminal and run:
git clone https://github.com/elijahkato/hng12_project0.git
cd hng12_project0

## Create a virtual environment:
Depending on your operating system, run one of the following:

Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate

Windows (PowerShell):
python -m venv venv
venv\Scripts\Activate.ps1

Mac / Linux (Terminal):
python -m venv venv
source venv/bin/activate

## Install dependencies:
pip install -r requirements.txt

Run the API:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Test the API:
Open a browser and go to: http://127.0.0.1:8000

Or use cURL: curl -X GET http://127.0.0.1:8000

Access API documentation:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc UI: http://127.0.0.1:8000/redoc

Deactivate the virtual environment when done:

## 🔗 Hire Python Developers
Looking for expert Python developers? [Click here] (https://hng.tech/hire/python-developers)


## 📌 API Documentation
### **GET /** 
#### **Response Format (200 OK)**:
```json
{
  "email": "elijahosas@gmail.com",
  "current_datetime": "2025-01-31T20:33:46+00:00",
  "github_url": "https://github.com/elijahkato/hng12_project0"
}
