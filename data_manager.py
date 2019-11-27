import connection


@connection.connection_handler
def get_data(cursor, data_table, id='', question_id='', answer_id=''):
    cursor.execute(f"""
                        SELECT * FROM {data_table}{" WHERE id = " + id if id else ''}
                        {" WHERE question_id = " + question_id if question_id else ''}
                        {" AND answer_id = " + answer_id if answer_id else ''};""")
    print(cursor.query)
    data = cursor.fetchall()
    return data


@connection.connection_handler
def sort_questions(cursor, order):
    cursor.execute(f"""
                    SELECT id, submission_time, view_number, vote_number, title, message, image
                    FROM question
                    {order};
                   """)
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def add_new_question(cursor, new_user_question):
    cursor.execute("""
    INSERT INTO question(title, message, submission_time)
    VALUES (%s, %s, CURRENT_TIMESTAMP(0))""", (new_user_question['question_title'], new_user_question['question']))


@connection.connection_handler
def add_new_answer(cursor, new_user_answer, question_id):
    cursor.execute("""
        INSERT INTO answer (question_id, message, submission_time)
        VALUES (%s, %s, CURRENT_TIMESTAMP(0))""", (question_id, new_user_answer['answer']))


@connection.connection_handler
def post_comment(cursor, new_comment, question_id, answer_id):
    cursor.execute("""
            INSERT INTO comment (question_id, answer_id, message, submission_time)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP (0))""", (question_id, answer_id, new_comment['comment']))


@connection.connection_handler
def post_question_comment(cursor, new_comment, question_id):
    cursor.execute("""
            INSERT INTO comment (question_id, message, submission_time)
            VALUES (%s, %s, CURRENT_TIMESTAMP (0))""", (question_id, new_comment['comment']))


@connection.connection_handler
def get_question_comments(cursor, question_id):
    cursor.execute(f"""

                        SELECT question.id, comment.message, comment.submission_time, comment.edited_count 
                        FROM question
                        JOIN comment ON question.id = comment.question_id
                        WHERE question.id = {question_id} AND comment.answer_id IS NULL;
                        """)
    question_comments = cursor.fetchall()
    return question_comments


@connection.connection_handler
def get_answer_comments(cursor, answer_id):
    cursor.execute(f"""
                        SELECT answer.id, comment.message, comment.submission_time, comment.edited_count 
                        FROM answer 
                        JOIN comment ON answer.id = comment.answer_id
                        WHERE answer.id = comment.answer_id;
                        """)
    answer_comments = cursor.fetchall()
    return answer_comments


@connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute(f"""
                       DELETE FROM comment
                       WHERE question_id = {question_id};
                       DELETE FROM answer 
                       WHERE question_id = {question_id};
                       DELETE FROM question
                       WHERE question.id = {question_id};
                       """)


@connection.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute(f""" 
                        DELETE FROM comment 
                        WHERE comment.answer_id = {answer_id};
                        DELETE FROM answer 
                        WHERE answer.id = {answer_id};
                        """)


@connection.connection_handler
def vote(cursor, data_table, up_or_down, question_or_answer_id):
    cursor.execute(f"""
                        UPDATE {data_table} 
                        SET vote_number = vote_number + {up_or_down}
                        WHERE question_id = {}
                        """)
