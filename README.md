📌 Project: Flask To-Do App
A simple web-based To-Do List application built with Python Flask, designed to help users manage tasks efficiently. It supports creating, viewing, updating, and deleting to-do items — all in a clean and responsive interface.

🚀 Features
Add new tasks
Mark tasks as complete/incomplete
Edit existing tasks
Delete tasks
Lightweight and fast UI using HTML/CSS (and optionally Bootstrap)
Deployed on Render for public access

🛠️ Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS, Bootstrap (optional)
Database: SQLite
Deployment: Render

📂 Project Structure
├── __pycache__/            # Python cache files (auto-generated)
├── app.py                  # Main Flask application
├── instance/
│   └── todo.db             # SQLite database file
├── Procfile                # Render deployment configuration
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates (Jinja2)
│   ├── about.html
│   ├── base.html
│   ├── index.html
│   └── update.htm


📦 How to Run Locally
git clone https://github.com/ananya1328/todo-flask.git
cd todo-flask
pip install -r requirements.txt
python app.py
