class Participant:
    def __init__(self, user_name,
                 question1,
                 question2,
                 answer1: 0,
                 answer2: 0,
                 score: 0):
        self._user_name = user_name
        self._question1 = question1
        self._question2 = question2
        self._answer1 = answer1
        self._answer2 = answer2
        self._score = score

    @property
    def user_name(self):
        return self._user_name

    @property
    def question1(self):
        return self._question1

    @property
    def question2(self):
        return self._question2

    @property
    def answer1(self):
        return self._answer1

    @property
    def answer2(self):
        return self._answer2

    @property
    def score(self):
        return self._score

    def __str__(self) -> str:
        return f"{self._user_name}, {self._question1}, {self._question2}, {self._answer1}," \
               f"{self._answer2}, {self._score}"