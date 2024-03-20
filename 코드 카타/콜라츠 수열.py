def solution(n):
    answer = []
    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    answer.append(n)
    return answer


a = 10000
# b = 1
# c = 2
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
print(result)
