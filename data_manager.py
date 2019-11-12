import connection

FIELDNAMES = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_FIELDNAMES = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


@connection.connection_handler
def get_all_questions(cursor):
    cursor.execute("""
                    SELECT id, submission_time, view_number, vote_number, title, message, image FROM question;
                   """)
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def add_new_question(cursor, new_user_question):
    cursor.execute("""
    INSERT INTO question(title, message)
    VALUES (%s, %s)""", (new_user_question['question_title'], new_user_question['question']))


@connection.connection_handler
def add_new_answer(cursor, new_user_answer, question_id):
    cursor.execute("""
        INSERT INTO answer (question_id, message)
        VALUES (%s, %s)""", (question_id, new_user_answer['answer']))


def get_answers():
    list_of_answers = []
    with open('sample_data/answer.csv', 'r') as answer_file:
        reader = csv.DictReader(answer_file)
        for line in reader:
            list_of_answers.append(dict(line))
    return list_of_answers
