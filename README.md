# Phase-4-Superheroes API

A RESTful API built with Flask for managing superheroes, their powers, and their associations. It allows you to create, retrieve, update, and delete (CRUD) hero and power data.

## Features

* Manage superhero details.
* Manage various superpowers.
* Assign powers to heroes with specific strength levels (Strong, Average, Weak).
* Uses Flask-SQLAlchemy for database interaction and Flask-Migrate for schema management.

## Technologies Used

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite (development database)

## Getting Started

Follow these steps to set up and run the project locally.

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url_here> # Replace with your actual repo URL
    cd Phase-4-Superheroes
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    # On Linux/macOS/WSL:
    source venv/bin/activate
    # On Windows (Command Prompt):
    # venv\Scripts\activate.bat
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup & Seeding

1.  **Set Flask App environment variable:**
    ```bash
    # On Linux/macOS/WSL:
    export FLASK_APP=app:create_app
    # On Windows (Command Prompt):
    # set FLASK_APP=app:create_app
    ```
2.  **Run database migrations:**
    ```bash
    flask db upgrade
    ```
3.  **Seed the database with sample data:**
    ```bash
    python seed.py
    ```

## Running the Application

Once setup is complete, start the Flask development server:

```bash
flask run