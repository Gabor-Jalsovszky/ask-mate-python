import connection

@connection.connection_handler
def get_data(cursor, data_table, question_id='', answer_id=''):
    cursor.execute(f"""
                        SELECT * FROM {data_table}{" WHERE question_id = " + question_id if question_id else ''}
                        {" AND answer_id = " + answer_id if answer_id else ''};""")
    print(cursor.query)
    data = cursor.fetchall()
    return data


@connection.connection_handler
def sort_questions(cursor, order):
    if order == 'Ascending_ID':
        cursor.execute("""
                        SELECT id, submission_time, view_number, vote_number, title, message, image FROM question;
                       """)
    elif order == 'Descending_ID':
        cursor.execute("""
                        SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                        ORDER BY id DESC; 
                        """)
    elif order == 'Ascending_Question':
        cursor.execute("""
                            SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                            ORDER BY title ASC; 
                            """)
    elif order == 'Descending_Question':
        cursor.execute("""
                            SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                            ORDER BY title DESC; 
                            """)
    elif order == 'Ascending_description':
        cursor.execute("""
                            SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                            ORDER BY message ASC; 
                            """)
    elif order == 'Descending_description':
        cursor.execute("""
                            SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                            ORDER BY message DESC; 
                            """)
    elif order == 'Ascending_date':
        cursor.execute("""
                            SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                            ORDER BY submission_time ASC; 
                            """)
    elif order == 'Descending_date':
        cursor.execute("""
                            SELECT id, submission_time, view_number, vote_number, title, message, image FROM question
                            ORDER BY submission_time DESC; 
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
            INSERT INTO comment (question_id, answer_id, message)
            VALUES (%s, %s, %s)""", (question_id, answer_id, new_comment['comment']))


@connection.connection_handler
def post_question_comment(cursor, new_comment, question_id):
    cursor.execute("""
            INSERT INTO comment (question_id, message)
            VALUES (%s, %s)""", (question_id, new_comment['comment']))





