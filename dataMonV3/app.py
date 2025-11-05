
from flask import Flask, render_template, request
import AnswerChecker  # use your existing code

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_answer():
    problem = request.form['problem']

    # Run the existing check_answer function
    result = AnswerChecker.check_answer(problem)

    # To show the correct answer when wrong, modify AnswerChecker to return more info
    if result is True:
        message = "✅ Correct!"
    elif result is False:
        message = "❌ Wrong! (Make sure you use format like 4+4=8)"
    else:
        message = "⚠️ Something went wrong."

    return render_template('result.html', problem=problem, message=message)

if __name__ == '__main__':
    app.run(debug=True)
