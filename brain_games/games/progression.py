from random import randint

RULES = 'What is missing in the progression?'


def make_progression(progression_len, min_step, max_step, min_num, max_num):
    first_num = randint(min_num, max_num)
    progression_step = randint(min_step, max_step)
    progression = [first_num, ]
    for i in range(progression_len):
        next_num = first_num + progression_step
        progression.append(next_num)
        first_num = next_num
    return progression


def question_and_correct_answer():
    progression = make_progression(10, 1, 10, 0, 30)
    random_index = randint(0, (len(progression) - 1))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = progression
    return question, str(correct_answer)