import random


def solution(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer


a, b = (random.randint(0, 100), random.randint(0, 100))

result = solution(a, b)
