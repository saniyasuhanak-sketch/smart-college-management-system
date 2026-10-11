# Smart College Management System

A full-stack Django-based college management system with role-based access for admin, faculty, and students.

## Features

- Admin dashboard with summary cards and charts
- Student and faculty management
- Department and course management
- Attendance tracking and percentages
- Examination and marks management
- Fee management and collection summaries
- Timetable and announcements
- Library management
- Profile and password management
- Role-based access control

## Stack

- Python 3.11+
- Django 5.x
- MySQL (configurable via `.env`)
- Bootstrap 5
- Chart.js

## Quick Start

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment
   ```bash
   cp .env.example .env
   ```
   Update values as needed.

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Create a superuser
   ```bash
   python manage.py createsuperuser
   ```

6. Seed demo data
   ```bash
   python manage.py seed_data
   ```

7. Start the server
   ```bash
   python manage.py runserver
   ```

## Default login

- Admin: use the superuser credentials you created.
- Demo users are created by `seed_data`.

## Notes

- MySQL is supported via environment variables.
- If `.env` is missing, the app falls back to SQLite for local development.
- Do not commit real secrets or production data.
