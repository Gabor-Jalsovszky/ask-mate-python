from flask import Flask, render_template, redirect, request, session

import data_manager

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def verify_user():
    if request.method == 'GET':
        return render_template('login.html')

    user_data = request.form
    valid = data_manager.verify_user(user_data['user_name'], user_data['password'])
    if valid is True:
        session['user_name'] = user_data['user_name']
        return redirect('/list')

    return redirect('/login')


@app.route('/list')
def route_list():
    if 'user_name' not in session:
        return redirect("/")
    user_name = session['user_name']
    order = request.args.get('sort')
    if order is None:
        questions = data_manager.sort_questions("ORDER BY id ASC")
    else:
        questions = data_manager.sort_questions(order)

    is_admin = True if user_name == 'Admin' else False

    return render_template("list.html", is_admin=is_admin, questions=questions)


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if 'user_name' in session:
        if request.method == 'POST':
            new_user_question = request.form
            data_manager.add_new_question(new_user_question)
            return redirect('/list')
        elif request.method == 'GET':
            return render_template("question.html")
    else:
        return redirect('/')


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_question(question_id):
    if 'user_name' in session:
        if request.method == 'GET':
            question = data_manager.get_data('question', question_id)
            answers = data_manager.get_data('answer', question_id=question_id)
            question_comments = data_manager.get_question_comments(question_id)
            answer_comments = data_manager.get_answer_comments(question_id)
            return render_template("question-only.html", question_id=int(question_id),
                                   question=question, answers=answers,
                                   question_comments=question_comments, answer_comments=answer_comments)
        elif request.method == 'POST':
            data_manager.delete_question(question_id)
            return redirect('/list')
    else:
        return redirect('/')


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(question_id):
    if 'user_name' in session:
        if request.method == 'POST':
            new_user_answer = request.form
            data_manager.add_new_answer(new_user_answer, question_id)
            return redirect('/question/' + question_id)
        questions = data_manager.get_data('question')
        return render_template("answer.html", question_id=int(question_id), questions=questions)
    else:
        return redirect('/')


@app.route('/question/<question_id>/<answer_id>/new-comment', methods=['GET', 'POST'])
def route_new_comment(question_id: int, answer_id: int):
    if 'user_name' in session:
        if request.method == 'POST':
            new_comment = request.form
            data_manager.post_comment(new_comment, question_id, answer_id)
            return redirect('/question/' + question_id)
        questions = data_manager.get_data('question')
        answers = data_manager.get_data('answer')
        return render_template("comment.html", question_id=int(question_id), answer_id=int(answer_id), questions=questions,
                               answers=answers)
    else:
        return redirect('/')


@app.route('/question/<question_id>/new-comment', methods=['GET', 'POST'])
def route_new_question_comment(question_id):
    if 'user_name' in session:
        if request.method == 'POST':
            new_comment = request.form
            data_manager.post_question_comment(new_comment, question_id)
            return redirect('/question/' + question_id)
        questions = data_manager.get_data('question')
        return render_template("comment_question.html", question_id=int(question_id), questions=questions)
    else:
        return redirect('/')


@app.route('/add-new-user', methods=['GET', 'POST'])
def add_new_user():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user_data = request.form
        data_manager.add_new_user(user_data['user_name'], user_data['password'])
        return redirect('/login')


@app.route('/question/<question_id>/<answer_id>/')
def route_delete_answer(question_id, answer_id):
    if 'user_name' in session:
        data_manager.delete_answer(answer_id)
        return redirect('/question/' + question_id)
    else:
        return redirect('/')


@app.route('/question/<question_id>/vote', methods=['POST'])
def route_vote(question_id):
    if 'user_name' in session:
        up_or_down = request.form
        data_manager.vote(question_id, int(up_or_down['up_or_down']))
        return redirect('/question/'+question_id)
    else:
        return redirect('/')


@app.route('/question/<question_id>/<answer_id>/vote', methods=['POST'])
def route_vote_answer(question_id, answer_id):
    if 'user_name' in session:
        up_or_down = request.form
        data_manager.vote_answer(answer_id, int(up_or_down['up_or_down']))
        return redirect('/question/'+question_id)
    else:
        return redirect('/')


@app.route('/list-users')
def route_list_users():
    if 'user_name' in session:
        user_name = session['user_name']
        if user_name == 'Admin':
            user_data = data_manager.get_users()
            return render_template('list_users.html', user_data=user_data)


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True,
    )

