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


def add_new_answer(answer):
    with open('sample_data/answer.csv', 'r') as answer_file:
        max_id = 0
        reader = csv.DictReader(answer_file)
        for line in reader:
            if int(line['id']) >= max_id:
                max_id = int(line['id'])
    with open('sample_data/answer.csv', 'a') as answer_file:

        writer = csv.DictWriter(answer_file, fieldnames=ANSWER_FIELDNAMES)

        writer.writerow({'id': int(max_id) + 1, 'message': answer['answer']})


def get_answers():
    list_of_answers = []
    with open('sample_data/answer.csv', 'r') as answer_file:
        reader = csv.DictReader(answer_file)
        for line in reader:
            list_of_answers.append(dict(line))
    return list_of_answers
