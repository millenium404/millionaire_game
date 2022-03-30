import random

def joker_1():
    correct_percent = random.randint(54, 82)
    answer_2_percent = round((100 - correct_percent) / 3)
    answer_3_percent = round((100 - correct_percent - answer_2_percent) / 1.4)
    answer_4_percent = 100 - answer_3_percent - answer_2_percent - correct_percent
    return correct_percent, answer_2_percent, answer_3_percent, answer_4_percent

print(joker_1())
