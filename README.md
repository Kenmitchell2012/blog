# Future Blogspot

A simple blog application built with Django, providing users with the ability to create, edit, and manage their blog posts.

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts (CRUD functionality)
- User profiles with profile management
- Responsive design for mobile and desktop

## Technologies Used

- Django
- Python
- Bootstrap
- SQLite (or your preferred database)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/future-blogspot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd future-blogspot
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- Users can register and log in to create and manage their blog posts.
- Navigate to the home page to view all posts.
- Click on "New Post" to create a new blog entry.
- Access user profiles to edit personal information and settings.
