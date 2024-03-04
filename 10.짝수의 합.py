import random


def solution(n):
    answer = 0
    for i in range(n // 2):
        answer += ((i + 1) * 2)
    return answer


a = random.randint(0, 1000)

result = solution(a)
