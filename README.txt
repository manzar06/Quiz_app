Online Quiz System

Simple quiz application built with Flask HTML CSS and JavaScript.

Features

- User registration and login
- Multiple choice questions
- Timer with warnings
- Auto score calculation
- Result display
- Quiz history

Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Seed database:
   python seed_data.py

3. Run app:
   python app.py

4. Open browser:
   Go to http://localhost:5000
   Login with admin/admin123

Files

- app.py - main Flask app
- seed_data.py - database setup
- requirements.txt - dependencies
- templates/ - HTML files
- static/css/ - styles
- static/js/ - JavaScript

Usage

1. Register or login
2. Select a quiz from dashboard
3. Answer questions
4. Timer counts down automatically
5. Submit to see results
6. View history in My Results

Database

- User table for accounts
- Quiz table for quiz info
- Question table for questions
- QuizResult table for scores

Notes

Basic setup for learning. For production:
- Hash passwords
- Add CSRF protection
- Use environment variables
- Validate inputs

