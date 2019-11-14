import connection


@connection.connection_handler
def get_all_questions(cursor, questions):
    if questions['sort'] == 'Ascending_ID':
        cursor.execute("""
                        SELECT id, submission_time, view_number, vote_number, title, message, image FROM question;
                       """)
        questions = cursor.fetchall()
        return questions
    elif questions['sort'] == 'Descending_ID':
        cursor.execute("""
                        SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                        ORDER BY id DESC; 
                        """)
        questions = cursor.fetchall()
        return questions


@connection.connection_handler
def add_new_question(cursor, new_user_question):
    cursor.execute("""
    INSERT INTO question(title, message, submission_time)
    VALUES (%s, %s, CURRENT_TIMESTAMP)""", (new_user_question['question_title'], new_user_question['question']))


@connection.connection_handler
def add_new_answer(cursor, new_user_answer, question_id):
    cursor.execute("""
        INSERT INTO answer (question_id, message, submission_time)
        VALUES (%s, %s, CURRENT_TIMESTAMP)""", (question_id, new_user_answer['answer']))


@connection.connection_handler
def get_answers(cursor):
    cursor.execute("""
                        SELECT id, submission_time, vote_number, question_id, message, image FROM answer;
                       """)
    answers = cursor.fetchall()
    return answers


@connection.connection_handler
def post_comment(cursor, new_comment, question_id, answer_id):
    cursor.execute("""
            INSERT INTO comment (question_id, answer_id, message)
            VALUES (%s, %s, %s)""", (question_id, answer_id, new_comment['comment']))


@connection.connection_handler
def post_question_comment(cursor, new_comment, question_id):
    cursor.execute("""
            INSERT INTO comment (question_id, message)
            VALUES (%s, %s)""", (question_id, new_comment['comment']))


@connection.connection_handler
def get_comments(cursor):
    cursor.execute("""
                        SELECT id, question_id, answer_id, message, submission_time, edited_count FROM comment;
                       """)
    comments = cursor.fetchall()
    return comments


