from app import app, db, User, Quiz, Question

def seed_database():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Create default user
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password='admin123')
            db.session.add(admin)
            db.session.commit()
            print("Created default user: admin/admin123")
        
        quizzes_data = [
            {
                'title': 'Python Basics Quiz',
                'description': 'Test your knowledge of Python programming fundamentals',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What is the correct way to create a list in Python?',
                        'option_a': 'list = (1, 2, 3)',
                        'option_b': 'list = [1, 2, 3]',
                        'option_c': 'list = {1, 2, 3}',
                        'option_d': 'list = <1, 2, 3>',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which keyword is used to define a function in Python?',
                        'option_a': 'func',
                        'option_b': 'function',
                        'option_c': 'def',
                        'option_d': 'define',
                        'question_type': 'single',
                        'correct_answer': 'C'
                    },
                    {
                        'question_text': 'Which of the following are mutable data types in Python?',
                        'option_a': 'List',
                        'option_b': 'Tuple',
                        'option_c': 'Dictionary',
                        'option_d': 'String',
                        'question_type': 'multiple',
                        'correct_answer': 'A,C'
                    },
                    {
                        'question_text': 'What does the len() function do?',
                        'option_a': 'Returns the length of a string or list',
                        'option_b': 'Returns the largest number',
                        'option_c': 'Returns the smallest number',
                        'option_d': 'Converts to lowercase',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'Which operator is used for exponentiation in Python?',
                        'option_a': '^',
                        'option_b': '**',
                        'option_c': 'exp',
                        'option_d': 'pow',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    }
                ]
            },
            {
                'title': 'JavaScript Fundamentals',
                'description': 'Test your JavaScript programming skills',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'Which keyword is used to declare a variable in ES6?',
                        'option_a': 'var',
                        'option_b': 'let',
                        'option_c': 'const',
                        'option_d': 'All of the above',
                        'question_type': 'single',
                        'correct_answer': 'D'
                    },
                    {
                        'question_text': 'What are the primitive data types in JavaScript?',
                        'option_a': 'String',
                        'option_b': 'Number',
                        'option_c': 'Boolean',
                        'option_d': 'Object',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C'
                    },
                    {
                        'question_text': 'What does === operator do in JavaScript?',
                        'option_a': 'Compares values and types',
                        'option_b': 'Compares only values',
                        'option_c': 'Assigns value',
                        'option_d': 'Checks if undefined',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'Which method is used to add elements to an array?',
                        'option_a': 'push()',
                        'option_b': 'pop()',
                        'option_c': 'shift()',
                        'option_d': 'unshift()',
                        'question_type': 'multiple',
                        'correct_answer': 'A,D'
                    },
                    {
                        'question_text': 'What is the output of: typeof null?',
                        'option_a': 'null',
                        'option_b': 'undefined',
                        'option_c': 'object',
                        'option_d': 'number',
                        'question_type': 'single',
                        'correct_answer': 'C'
                    }
                ]
            },
            {
                'title': 'HTML & CSS Basics',
                'description': 'Test your knowledge of HTML and CSS',
                'time_limit': 480,
                'questions': [
                    {
                        'question_text': 'Which HTML tag is used for the largest heading?',
                        'option_a': '<h6>',
                        'option_b': '<h1>',
                        'option_c': '<head>',
                        'option_d': '<header>',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which CSS properties are used for layout?',
                        'option_a': 'display',
                        'option_b': 'position',
                        'option_c': 'color',
                        'option_d': 'flexbox',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    },
                    {
                        'question_text': 'What does CSS stand for?',
                        'option_a': 'Computer Style Sheets',
                        'option_b': 'Cascading Style Sheets',
                        'option_c': 'Creative Style Sheets',
                        'option_d': 'Colorful Style Sheets',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which HTML attribute is used to define inline styles?',
                        'option_a': 'styles',
                        'option_b': 'style',
                        'option_c': 'class',
                        'option_d': 'font',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'What are valid CSS selectors?',
                        'option_a': 'Class selector',
                        'option_b': 'ID selector',
                        'option_c': 'Element selector',
                        'option_d': 'Attribute selector',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C,D'
                    }
                ]
            },
            {
                'title': 'General Knowledge',
                'description': 'Test your general knowledge',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What is the capital of France?',
                        'option_a': 'London',
                        'option_b': 'Berlin',
                        'option_c': 'Paris',
                        'option_d': 'Madrid',
                        'question_type': 'single',
                        'correct_answer': 'C'
                    },
                    {
                        'question_text': 'Which of these are planets in our solar system?',
                        'option_a': 'Mars',
                        'option_b': 'Jupiter',
                        'option_c': 'Pluto',
                        'option_d': 'Venus',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    },
                    {
                        'question_text': 'Who wrote Romeo and Juliet?',
                        'option_a': 'Charles Dickens',
                        'option_b': 'William Shakespeare',
                        'option_c': 'Jane Austen',
                        'option_d': 'Mark Twain',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'What are the primary colors?',
                        'option_a': 'Red',
                        'option_b': 'Blue',
                        'option_c': 'Green',
                        'option_d': 'Yellow',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    },
                    {
                        'question_text': 'What is the largest ocean on Earth?',
                        'option_a': 'Atlantic Ocean',
                        'option_b': 'Indian Ocean',
                        'option_c': 'Arctic Ocean',
                        'option_d': 'Pacific Ocean',
                        'question_type': 'single',
                        'correct_answer': 'D'
                    }
                ]
            },
            {
                'title': 'Mathematics Quiz',
                'description': 'Test your math skills',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What is 15 + 27?',
                        'option_a': '40',
                        'option_b': '42',
                        'option_c': '44',
                        'option_d': '45',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which of these are prime numbers?',
                        'option_a': '2',
                        'option_b': '4',
                        'option_c': '7',
                        'option_d': '9',
                        'question_type': 'multiple',
                        'correct_answer': 'A,C'
                    },
                    {
                        'question_text': 'What is the square root of 64?',
                        'option_a': '6',
                        'option_b': '7',
                        'option_c': '8',
                        'option_d': '9',
                        'question_type': 'single',
                        'correct_answer': 'C'
                    },
                    {
                        'question_text': 'What is the value of π (pi) approximately?',
                        'option_a': '3.14',
                        'option_b': '3.14159',
                        'option_c': '22/7',
                        'option_d': 'All of the above',
                        'question_type': 'single',
                        'correct_answer': 'D'
                    },
                    {
                        'question_text': 'Which shapes have 4 sides?',
                        'option_a': 'Square',
                        'option_b': 'Rectangle',
                        'option_c': 'Triangle',
                        'option_d': 'Rhombus',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    }
                ]
            },
            {
                'title': 'Science Quiz',
                'description': 'Test your science knowledge',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What is the chemical symbol for water?',
                        'option_a': 'H2O',
                        'option_b': 'CO2',
                        'option_c': 'O2',
                        'option_d': 'NaCl',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'Which of these are states of matter?',
                        'option_a': 'Solid',
                        'option_b': 'Liquid',
                        'option_c': 'Gas',
                        'option_d': 'Plasma',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C,D'
                    },
                    {
                        'question_text': 'What is the speed of light?',
                        'option_a': '300,000 km/s',
                        'option_b': '150,000 km/s',
                        'option_c': '450,000 km/s',
                        'option_d': '200,000 km/s',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'Which planets are known as gas giants?',
                        'option_a': 'Jupiter',
                        'option_b': 'Saturn',
                        'option_c': 'Earth',
                        'option_d': 'Neptune',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    },
                    {
                        'question_text': 'What is the smallest unit of matter?',
                        'option_a': 'Molecule',
                        'option_b': 'Atom',
                        'option_c': 'Electron',
                        'option_d': 'Proton',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    }
                ]
            },
            {
                'title': 'World History',
                'description': 'Test your knowledge of world history',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'In which year did World War II end?',
                        'option_a': '1943',
                        'option_b': '1944',
                        'option_c': '1945',
                        'option_d': '1946',
                        'question_type': 'single',
                        'correct_answer': 'C'
                    },
                    {
                        'question_text': 'Which of these were ancient civilizations?',
                        'option_a': 'Roman Empire',
                        'option_b': 'Ancient Egypt',
                        'option_c': 'United States',
                        'option_d': 'Maya Civilization',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    },
                    {
                        'question_text': 'Who was the first person to walk on the moon?',
                        'option_a': 'Buzz Aldrin',
                        'option_b': 'Neil Armstrong',
                        'option_c': 'Michael Collins',
                        'option_d': 'Yuri Gagarin',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which events happened in the 20th century?',
                        'option_a': 'World War I',
                        'option_b': 'World War II',
                        'option_c': 'Fall of Berlin Wall',
                        'option_d': 'American Civil War',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C'
                    },
                    {
                        'question_text': 'The Renaissance period started in which country?',
                        'option_a': 'France',
                        'option_b': 'Germany',
                        'option_c': 'Italy',
                        'option_d': 'Spain',
                        'question_type': 'single',
                        'correct_answer': 'C'
                    }
                ]
            },
            {
                'title': 'Geography Quiz',
                'description': 'Test your geography knowledge',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What is the longest river in the world?',
                        'option_a': 'Amazon',
                        'option_b': 'Nile',
                        'option_c': 'Mississippi',
                        'option_d': 'Yangtze',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which countries are in Europe?',
                        'option_a': 'France',
                        'option_b': 'Germany',
                        'option_c': 'Brazil',
                        'option_d': 'Italy',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,D'
                    },
                    {
                        'question_text': 'What is the highest mountain in the world?',
                        'option_a': 'K2',
                        'option_b': 'Mount Everest',
                        'option_c': 'Kilimanjaro',
                        'option_d': 'Matterhorn',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which are the seven continents?',
                        'option_a': 'Asia',
                        'option_b': 'Africa',
                        'option_c': 'Antarctica',
                        'option_d': 'Australia',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C,D'
                    },
                    {
                        'question_text': 'What is the smallest country in the world?',
                        'option_a': 'Monaco',
                        'option_b': 'Vatican City',
                        'option_c': 'San Marino',
                        'option_d': 'Liechtenstein',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    }
                ]
            },
            {
                'title': 'Computer Science',
                'description': 'Test your computer science fundamentals',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What does CPU stand for?',
                        'option_a': 'Central Processing Unit',
                        'option_b': 'Computer Personal Unit',
                        'option_c': 'Central Program Utility',
                        'option_d': 'Computer Processing Unit',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'Which are programming paradigms?',
                        'option_a': 'Object-Oriented',
                        'option_b': 'Functional',
                        'option_c': 'Procedural',
                        'option_d': 'Declarative',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C,D'
                    },
                    {
                        'question_text': 'What is the time complexity of binary search?',
                        'option_a': 'O(n)',
                        'option_b': 'O(log n)',
                        'option_c': 'O(n²)',
                        'option_d': 'O(1)',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which data structures use LIFO principle?',
                        'option_a': 'Stack',
                        'option_b': 'Queue',
                        'option_c': 'Array',
                        'option_d': 'Tree',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'What are valid HTTP methods?',
                        'option_a': 'GET',
                        'option_b': 'POST',
                        'option_c': 'PUT',
                        'option_d': 'DELETE',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C,D'
                    }
                ]
            },
            {
                'title': 'Web Development',
                'description': 'Test your web development knowledge',
                'time_limit': 600,
                'questions': [
                    {
                        'question_text': 'What does HTTP stand for?',
                        'option_a': 'HyperText Transfer Protocol',
                        'option_b': 'HyperText Transport Protocol',
                        'option_c': 'HyperText Transfer Process',
                        'option_d': 'HyperText Transport Process',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    },
                    {
                        'question_text': 'Which are frontend frameworks?',
                        'option_a': 'React',
                        'option_b': 'Angular',
                        'option_c': 'Vue',
                        'option_d': 'Django',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B,C'
                    },
                    {
                        'question_text': 'What is the purpose of CSS?',
                        'option_a': 'Structure web pages',
                        'option_b': 'Style web pages',
                        'option_c': 'Add interactivity',
                        'option_d': 'Store data',
                        'question_type': 'single',
                        'correct_answer': 'B'
                    },
                    {
                        'question_text': 'Which HTTP status codes indicate success?',
                        'option_a': '200',
                        'option_b': '201',
                        'option_c': '404',
                        'option_d': '500',
                        'question_type': 'multiple',
                        'correct_answer': 'A,B'
                    },
                    {
                        'question_text': 'What is REST API?',
                        'option_a': 'Representational State Transfer',
                        'option_b': 'Remote State Transfer',
                        'option_c': 'Representational Server Transfer',
                        'option_d': 'Remote Server Transfer',
                        'question_type': 'single',
                        'correct_answer': 'A'
                    }
                ]
            }
        ]
        
        for quiz_data in quizzes_data:
            if not Quiz.query.filter_by(title=quiz_data['title']).first():
                quiz = Quiz(
                    title=quiz_data['title'],
                    description=quiz_data['description'],
                    time_limit=quiz_data['time_limit']
                )
                db.session.add(quiz)
                db.session.flush()
                
                for q_data in quiz_data['questions']:
                    question = Question(
                        quiz_id=quiz.id,
                        question_text=q_data['question_text'],
                        option_a=q_data['option_a'],
                        option_b=q_data['option_b'],
                        option_c=q_data['option_c'],
                        option_d=q_data['option_d'],
                        question_type=q_data.get('question_type', 'single'),
                        correct_answer=q_data['correct_answer']
                    )
                    db.session.add(question)
                
                db.session.commit()
                print(f"Created quiz: {quiz_data['title']} with {len(quiz_data['questions'])} questions")
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
