import csv

def get_all_questions():
    with open('sample_data/question.csv', 'r') as questions_file:
        reader = csv.DictReader(questions_file)
        questions = list(reader)
    return questions

def add_new_question():

    return

def add_new_answer():

    return