def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer


a = 2
b = 10
# c = 3
result = solution(a, b)
print(result)
