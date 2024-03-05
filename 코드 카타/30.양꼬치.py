def solution(n, k):
    answer = (n * 12000) + ((k - (n // 10)) * 2000)
    return answer


a = 64
b = 6
# c = 3
result = solution(a, b)
print(result)
