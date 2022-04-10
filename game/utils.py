import random
from .models import Question


def generate_questions_list():
    easy_qlist, normal_qlist, hard_qlist, qlist = [], [], [], []
    easy = Question.objects.filter(difficulty='easy')
    normal = Question.objects.filter(difficulty='normal')
    hard = Question.objects.filter(difficulty='hard')
    for item in easy:
        easy_qlist.append(item.id)
    while len(easy_qlist) > 5:
        easy_qlist.remove(random.choice(easy_qlist))
    random.shuffle(easy_qlist)
    for item in normal:
        normal_qlist.append(item.id)
    while len(normal_qlist) > 5:
        normal_qlist.remove(random.choice(normal_qlist))
    random.shuffle(normal_qlist)
    for item in hard:
        hard_qlist.append(item.id)
    while len(hard_qlist) > 5:
        hard_qlist.remove(random.choice(hard_qlist))
    random.shuffle(hard_qlist)
    qlist = easy_qlist + normal_qlist + hard_qlist
    return qlist

def string_to_list(string):
    string = string.lstrip('[')
    string = string.rstrip(']')
    string = string.split(', ')
    questions_id_list = [int(num) for num in string if num.isdigit()]
    return questions_id_list

def joker_public_func(correct_answer, answer_2, answer_3, answer_4):
    correct_answer, answer_2, answer_3, answer_4
    correct_percent = random.randint(54, 82)
    answer_2_percent = round((100 - correct_percent) / 3)
    answer_3_percent = round((100 - correct_percent - answer_2_percent) / 1.4)
    answer_4_percent = 100 - answer_3_percent - answer_2_percent - correct_percent
    correct_answer_string = str(correct_percent) + '% ' + correct_answer
    answer_2_string = str(answer_2_percent) + '% ' + answer_2
    answer_3_string = str(answer_3_percent) + '% ' + answer_3
    answer_4_string = str(answer_4_percent) + '% ' + answer_4
    return correct_answer_string, answer_2_string, answer_3_string, answer_4_string
