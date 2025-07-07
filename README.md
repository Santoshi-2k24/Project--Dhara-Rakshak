# Project Dhara-Rakshak

Dhara-Rakshak is a land registration and verification system to prevent fake land sales. Built using Django, it enables officers to register new land records, search for existing ones, and verify ownership with Aadhaar and document numbers.

## Features
- Officer login and dashboard
- Enter new land registration details
- Search existing records for ownership verification
- User-friendly interface

## Technologies Used
- Python
- Django
- HTML/CSS
- JavaScript (for frontend enhancements)

## How to Run
```bash
git clone https://github.com/Santoshi-2k24/Project--Dhara-Rakshak.git
cd Project--Dhara-Rakshak
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
