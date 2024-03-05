def solution(num, n):
    if num % n == 0:
        answer = 1
    else:
        answer = 0

    return answer

a = 98
b = 2
# c = 3
result = solution(a, b)
print(result)
