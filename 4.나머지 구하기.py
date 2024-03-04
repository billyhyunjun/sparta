import random


def solution(num1, num2):
    answer = num1 % num2
    return answer


a, b = (random.randint(0, 100), random.randint(0, 100))

result = solution(a, b)
