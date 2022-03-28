import random
from. models import Question


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
        easy_qlist.append(item.id)
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
