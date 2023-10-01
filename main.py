import csv
import json
import random
from pathlib import Path
import json
from participant import Participant
from input_handler import insert_participant_name
from ui import calculate_participant_points, insert_json_data
q = [
    ('2+2=?', 4, 5),
    ('2-2=?', 0, 6),
    ('2*2=?', 4, 7),
    ('2/2=?', 1, 8)
]


points = 0
questions = []
reply = []
name = insert_participant_name()

data_participant = calculate_participant_points(q, questions, reply, points)
p = Participant(name, data_participant[0][0], data_participant[0][1], data_participant[1][0], data_participant[1][1],
                data_participant[2])
print(p)

insert_json_data(name, data_participant[2])

