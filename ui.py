import random
from typing import Tuple
import json


def calculate_participant_points(q, questions, reply, points) -> Tuple:
    questions = []
    reply = []
    points = 0
    for i in range(2):
        question = random.choice(q)
        questions.append(question[0])
        print(question[0])
        res = int(input('Please, enter the result!\n '))
        reply.append(res)
        if res == question[1]:
            print('True')
            points = points + question[2]
            print(points)
    print(points)
    data_participant = (questions, reply, points)
    return data_participant


def insert_json_data(name: str, d_part: int):
    with open('data.json', 'w') as f:
        json.dump({name: d_part}, f)

