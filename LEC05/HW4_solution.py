import random


def generate_score(subjects, student_count):
    global score
    score = [{sub: random.randint(0, 100) for sub in subjects} for n in range(student_count)]
    pass


def process_score(score):
    global result, sub_avg
    result = [{'AVG': sum(e.values()) / len(e.keys()), 'TOTAL': sum(e.values)} for e in score]
    sub_avg = {sub: sum(e[sub] for e in score)/len(score) for sub in score[0].keys()}
    pass


def print_score():
    pass


generate_score(['KOR', 'ENG', 'MATH'],20)
process_score()
print_score()

