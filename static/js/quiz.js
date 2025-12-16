document.addEventListener('DOMContentLoaded', function() {
    const quizForm = document.getElementById('quiz-form');
    const timerElement = document.getElementById('timer-text');
    const timerContainer = document.getElementById('timer');
    const quizId = document.getElementById('quiz-id').value;
    const timeLimit = parseInt(document.getElementById('time-limit').value) || 600; // Default 10 minutes
    
    let timeRemaining = timeLimit;
    let startTime = Date.now();
    let timerInterval;
    
    // Initialize timer
    function updateTimer() {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        timerElement.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        // Add warning classes
        if (timeRemaining <= 60) {
            timerContainer.classList.add('danger');
            timerContainer.classList.remove('warning');
        } else if (timeRemaining <= 300) {
            timerContainer.classList.add('warning');
        }
        
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            alert('Time is up! Submitting your quiz automatically.');
            submitQuiz();
        } else {
            timeRemaining--;
        }
    }
    
    // Start timer
    timerInterval = setInterval(updateTimer, 1000);
    updateTimer();
    
    // Handle form submission
    quizForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (confirm('Are you sure you want to submit your quiz? You cannot change your answers after submission.')) {
            submitQuiz();
        }
    });
    
    function submitQuiz() {
        clearInterval(timerInterval);
        
        // Collect answers
        const answers = {};
        const questionCards = document.querySelectorAll('.question-card');
        
        questionCards.forEach(card => {
            const questionId = card.dataset.questionId;
            const radioOption = card.querySelector('input[type="radio"]:checked');
            const checkboxOptions = card.querySelectorAll('input[type="checkbox"]:checked');
            
            if (radioOption) {
                // Single choice question
                answers[questionId] = radioOption.value;
            } else if (checkboxOptions.length > 0) {
                // Multiple choice question - collect all checked values
                answers[questionId] = Array.from(checkboxOptions).map(cb => cb.value);
            }
        });
        
        // Calculate time taken
        const timeTaken = timeLimit - timeRemaining;
        
        // Disable form
        quizForm.querySelectorAll('input, button').forEach(el => {
            el.disabled = true;
        });
        
        // Show loading
        const submitBtn = quizForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Submitting...';
        submitBtn.disabled = true;
        
        // Submit to server
        fetch('/submit_quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                quiz_id: quizId,
                answers: answers,
                time_taken: timeTaken
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Error: ' + data.error);
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            } else {
                // Redirect to result page
                // We'll need to get the result ID from the response or create a result page route
                // For now, show result in alert and redirect to dashboard
                const percentage = data.percentage;
                let message = `Quiz Submitted!\n\n`;
                message += `Score: ${data.score}/${data.total_questions}\n`;
                message += `Percentage: ${percentage}%\n`;
                message += `Time Taken: ${Math.floor(data.time_taken / 60)}:${(data.time_taken % 60).toString().padStart(2, '0')}\n\n`;
                
                if (percentage >= 80) {
                    message += 'Excellent! You did great!';
                } else if (percentage >= 60) {
                    message += 'Good job! Keep practicing!';
                } else if (percentage >= 40) {
                    message += 'Not bad, but you can do better!';
                } else {
                    message += 'Keep studying and try again!';
                }
                
                // Redirect to result page
                if (data.result_id) {
                    window.location.href = '/result/' + data.result_id;
                } else {
                    alert(message);
                    window.location.href = '/dashboard';
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while submitting the quiz. Please try again.');
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        });
    }
    
    // Prevent accidental page refresh
    window.addEventListener('beforeunload', function(e) {
        if (timeRemaining > 0 && timeRemaining < timeLimit) {
            e.preventDefault();
            e.returnValue = 'Are you sure you want to leave? Your progress will be lost.';
            return e.returnValue;
        }
    });
});

