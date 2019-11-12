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
        new_user_question = request.form
        data_manager.add_new_question(new_user_question)
        return redirect('/list')
    elif request.method == 'GET':
        return render_template("question.html")


@app.route('/question/<question_id>')
def route_question(question_id):
    questions = data_manager.get_all_questions()
    #answers = data_manager.get_answers()
    return render_template("question-only.html", question_id=int(question_id), questions=questions)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(question_id):
    if request.method == 'POST':
        new_user_answer = request.form
        data_manager.add_new_answer(new_user_answer, question_id)
        return redirect('/question/<question_id>')

    questions = data_manager.get_all_questions()
    return render_template("answer.html", question_id=int(question_id), questions=questions)


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True,
    )
