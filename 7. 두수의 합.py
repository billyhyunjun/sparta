import random


def solution(num1, num2):
    answer = num1 + num2
    return answer


a, b = (random.randint(-50000, 50000), random.randint(-50000, 50000))

result = solution(a, b)
