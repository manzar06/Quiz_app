from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    quiz_results = db.relationship('QuizResult', backref='user', lazy=True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    time_limit = db.Column(db.Integer, default=600)  # in seconds
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref='quiz', lazy=True, cascade='all, delete-orphan')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    question_type = db.Column(db.String(20), default='single')  # 'single' or 'multiple'
    correct_answer = db.Column(db.String(10), nullable=False)  # 'A', 'B', 'C', 'D' or 'A,B', 'A,B,C' etc.

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Integer)  # in seconds
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    quiz = db.relationship('Quiz', backref='results')

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    quizzes = Quiz.query.all()
    # Get user's previous results for each quiz
    user_results = {}
    results = QuizResult.query.filter_by(user_id=session['user_id']).all()
    for result in results:
        if result.quiz_id not in user_results:
            user_results[result.quiz_id] = []
        user_results[result.quiz_id].append(result)
    
    # Sort results by date for each quiz (most recent first)
    for quiz_id in user_results:
        user_results[quiz_id].sort(key=lambda x: x.completed_at, reverse=True)
    
    return render_template('dashboard.html', quizzes=quizzes, user_results=user_results)

@app.route('/quiz/<int:quiz_id>')
def quiz(quiz_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    
    if not questions:
        flash('No questions available for this quiz', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('quiz.html', quiz=quiz, questions=questions)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.json
    quiz_id = data.get('quiz_id')
    answers = data.get('answers', {})
    time_taken = data.get('time_taken', 0)
    
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    
    score = 0
    total_questions = len(questions)
    
    for question in questions:
        user_answer = answers.get(str(question.id))
        if not user_answer:
            continue
            
        if question.question_type == 'multiple':
            # For multiple choice, user_answer is a list like ['A', 'B']
            # correct_answer is a string like 'A,B' or 'A,B,C'
            user_answers = sorted([a.upper().strip() for a in user_answer if a])
            correct_answers = sorted([a.upper().strip() for a in question.correct_answer.split(',')])
            if user_answers == correct_answers:
                score += 1
        else:
            # Single choice question
            if user_answer.upper().strip() == question.correct_answer.upper().strip():
                score += 1
    
    # Save result
    result = QuizResult(
        user_id=session['user_id'],
        quiz_id=quiz_id,
        score=score,
        total_questions=total_questions,
        time_taken=time_taken
    )
    db.session.add(result)
    db.session.commit()
    
    percentage = (score / total_questions * 100) if total_questions > 0 else 0
    
    return jsonify({
        'score': score,
        'total_questions': total_questions,
        'percentage': round(percentage, 2),
        'time_taken': time_taken,
        'result_id': result.id
    })

@app.route('/result/<int:result_id>')
def result(result_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    result = QuizResult.query.get_or_404(result_id)
    
    if result.user_id != session['user_id']:
        flash('Access denied', 'error')
        return redirect(url_for('dashboard'))
    
    quiz = Quiz.query.get(result.quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz.id).all()
    
    return render_template('result.html', result=result, quiz=quiz, questions=questions)

@app.route('/my_results')
def my_results():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    results = QuizResult.query.filter_by(user_id=session['user_id']).order_by(QuizResult.completed_at.desc()).all()
    return render_template('my_results.html', results=results)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

