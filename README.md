# Credit & Debit Tracker

A beginner-friendly Django app for personal credit/debit tracking with authentication, owner-scoped transactions, reports, tutorials, and Django Admin. SQLite is configured by default.

## Setup

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the app and http://127.0.0.1:8000/admin/ for administration. The admin uses Django's built-in Users, Groups, and Permissions screens. Assign `is_staff` only to trusted administrative accounts. Tutorials can be created in the Tutorials section of the admin and appear publicly after publication.

Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, and `DJANGO_ALLOWED_HOSTS` in the environment before deployment. For image uploads, install the Pillow dependency.

## Features

- Register, login/logout, password validation and password change
- Credit and debit forms, filters, edit/delete, with user ownership enforced in every query
- Dashboard totals, current balance and recent transactions
- Category report and published tutorial list/detail pages
- Tutorial and transaction admin configuration; built-in User/Group/Permission administration
