import random


def solution(num1, num2):
    answer = divmod(num1, num2)
    return answer[0]


a, b = (random.randint(0, 100), random.randint(0, 100))

result = solution(a, b)
