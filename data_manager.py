import connection
import bcrypt


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@connection.connection_handler
def add_new_user(cursor, user_name, password):
    hashed_password = hash_password(password)
    cursor.execute("""
            INSERT INTO users (name, password)
            VALUES (%s, %s);""", (user_name, hashed_password))


@connection.connection_handler
def verify_user(cursor, user_name, password):
    try:
        cursor.execute(""" 
                        SELECT password FROM users 
                        WHERE name = %(user_name)s;""", {'user_name': user_name})
        saved_password = cursor.fetchone()['password']
        is_matching = verify_password(password, saved_password)
        return is_matching
    except TypeError:
        return False


@connection.connection_handler
def get_data(cursor, data_table, id='', question_id='', answer_id=''):
    cursor.execute(f"""
                        SELECT * FROM {data_table}{" WHERE id = " + id if id else ''}
                        {" WHERE question_id = " + question_id if question_id else ''}
                        {" AND answer_id = " + answer_id if answer_id else ''}
                        ORDER BY id;
                        """)
    data = cursor.fetchall()
    return data


@connection.connection_handler
def sort_questions(cursor, order):
    cursor.execute("""
                    SELECT id, submission_time, view_number, vote_number, title, message, image
                    FROM question {}""".format(order)
                   )
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def add_new_question(cursor, new_user_question):
    cursor.execute("""
                    INSERT INTO question(title, message, submission_time, vote_number)
                    VALUES (%s, %s, CURRENT_TIMESTAMP(0), 0)""",
                   (new_user_question['question_title'], new_user_question['question']))


@connection.connection_handler
def add_new_answer(cursor, new_user_answer, question_id):
    cursor.execute("""
                    INSERT INTO answer (question_id, message, submission_time, vote_number)
                    VALUES (%s, %s, CURRENT_TIMESTAMP(0), 0)""", (question_id, new_user_answer['answer']))


@connection.connection_handler
def post_comment(cursor, new_comment, question_id, answer_id):
    cursor.execute("""
                    INSERT INTO comment (question_id, answer_id, message, submission_time)
                    VALUES (%s, %s, %s, CURRENT_TIMESTAMP(0))""", (question_id, answer_id, new_comment['comment'])
                   )


@connection.connection_handler
def post_question_comment(cursor, new_comment, question_id):
    cursor.execute("""
                    INSERT INTO comment (question_id, message, submission_time)
                    VALUES (%s, %s, CURRENT_TIMESTAMP(0))""", (question_id, new_comment['comment'])
                   )


@connection.connection_handler
def get_question_comments(cursor, question_id):
    cursor.execute("""
                    SELECT question.id, comment.message, comment.submission_time, comment.edited_count 
                    FROM question
                    JOIN comment ON question.id = comment.question_id
                    WHERE question.id = %(question_id)s
                    AND comment.answer_id IS NULL;
                    """, {'question_id': question_id}
                   )
    question_comments = cursor.fetchall()
    return question_comments


@connection.connection_handler
def get_answer_comments(cursor, question_id):
    cursor.execute("""
                    SELECT answer_id, comment.message, comment.submission_time, comment.edited_count 
                    FROM comment
                    WHERE question_id = %(question_id)s
                    AND comment.answer_id IS NOT NULL;
                    """, {'question_id': question_id}
                   )
    answer_comments = cursor.fetchall()
    return answer_comments


@connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("""
                    DELETE FROM comment
                    WHERE question_id = %(question_id)s;
                    DELETE FROM answer 
                    WHERE question_id = %(question_id)s;
                    DELETE FROM question
                    WHERE question.id = %(question_id)s;
                   """, {'question_id': question_id}
                   )


@connection.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute(""" 
                    DELETE FROM comment 
                    WHERE comment.answer_id = %(answer_id)s;
                    DELETE FROM answer 
                    WHERE answer.id = %(answer_id)s;
                    """, {'answer_id': answer_id}
                   )


@connection.connection_handler
def vote(cursor, question_id, up_or_down):
    cursor.execute("""
                    UPDATE question 
                    SET vote_number = vote_number + %(up_or_down)s
                    WHERE question.id = %(question_id)s
                    """, {'up_or_down': up_or_down, 'question_id': question_id}
                   )


@connection.connection_handler
def vote_answer(cursor, answer_id, up_or_down):
    cursor.execute("""
                    UPDATE answer
                    SET vote_number = vote_number + %(up_or_down)s
                    WHERE answer.id = %(answer_id)s
                    """, {'up_or_down': up_or_down, 'answer_id': answer_id}
                   )


@connection.connection_handler
def get_users(cursor):
    cursor.execute("""
                    SELECT id, name, password 
                    FROM users;
                    """
                   )
    user_data = cursor.fetchall()
    return user_data
