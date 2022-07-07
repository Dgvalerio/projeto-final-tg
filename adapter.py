import random

import numpy as np


def games_adapter():
    quizzes = np.zeros((1000000, 81), np.str_)
    solutions = np.zeros((1000000, 81), np.str_)

    for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = 'x' if q == '0' else q
            solutions[i, j] = s

    quizzes = quizzes.reshape((-1, 9, 9))
    # solutions = solutions.reshape((-1, 9, 9))

    return quizzes


def get_random_game():
    quizzes = games_adapter()

    return quizzes[random.randint(0, 999999)]
