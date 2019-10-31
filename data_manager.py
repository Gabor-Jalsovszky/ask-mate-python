import csv

FIELDNAMES = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

def get_all_questions():
    list_of_questions = []
    with open('sample_data/question.csv', 'r') as questions_file:
        reader = csv.DictReader(questions_file)
        for line in reader:
            list_of_questions.append(dict(line))
    return list_of_questions

def add_new_question(question):
    with open('sample_data/question.csv', 'r') as questions_file:
        max_id = 0
        reader = csv.DictReader(questions_file)
        for line in reader:
            if int(line['id']) >= max_id:
                max_id = int(line['id'])
    with open('sample_data/question.csv', 'a') as questions_file:

        writer = csv.DictWriter(questions_file, fieldnames=fieldnames)

        writer = csv.DictWriter(questions_file, fieldnames=FIELDNAMES)

        writer.writerow({'id': int(max_id) + 1, 'title': question['question_title'], 'message': question['question']})

def add_new_answer():

    return