import random


def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer


a, b = (random.randint(0, 10000), random.randint(0, 10000))

result = solution(a, b)
