from flask import Flask, render_template, redirect, request

import data_manager

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    questions = data_manager.get_all_questions()
    return render_template("list.html", questions=questions)


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        return redirect('/list')
    elif request.method == 'GET':
        return render_template("question.html")


@app.route('/question/<question_id>')
def route_question(question_id):
    return render_template("answer.html", question_id)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(question_id):
    if request.method == 'POST':
        return redirect('/question/<question_id>')

    return render_template("answer.html", question_id=question_id)


if __name__ == '__main__':
    app.run(
        port=8000,
        debug=True,
    )
