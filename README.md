# Web Developer Portfolio

A Django-based portfolio website showcasing projects and web development work.  
This project is built with **Python (Django framework)** and uses SQLite as the database.

---

## 🚀 Features
- Portfolio website built using Django
- Project showcase with details (PDFs, media files, etc.)
- Admin panel for managing projects and content
- REST-friendly structure (can be extended for APIs)

---

## 📂 Project Structure
```
Web_Developer_Portfolio/
│── Hello/                  # Main Django project folder
│   ├── settings.py         # Project settings
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py/asgi.py     # Deployment files
│
│── home/                   # Portfolio app
│   ├── models.py           # Database models for projects
│   ├── views.py            # Business logic
│   ├── urls.py             # App-level routes
│   ├── admin.py            # Admin configurations
│   └── migrations/         # Database migrations
│
│── media/                  # Uploaded files (project PDFs, images)
│── db.sqlite3              # SQLite database
│── manage.py               # Django management script
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/Web_Developer_Portfolio.git
   cd Web_Developer_Portfolio/Hello
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)

   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Now visit: `http://127.0.0.1:8000/`

---

## 📸 Screenshots
(Add screenshots of your portfolio website here)

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, Django templates
- **Other:** Django Admin, Static/Media handling


