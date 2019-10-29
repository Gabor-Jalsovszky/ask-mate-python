from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def route_list():
    return render_template("list.html")

@app.route('/add-question')
def route_add_question():
    return render_template("question.html")

@app.route('/question/<question_id>')
def route_question(question_id):
    return render_template("question.html")

@app.route('/question/<question_id>/new-answer')
def route_new_answer(question_id):
    return render_template("question.html")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )