import random


def solution(num):
    if num % 2 == 0 :
        answer = "Even"
    else:
        answer = "Odd"
    return answer


a = random.randint(0, 1000)

result = solution(a)