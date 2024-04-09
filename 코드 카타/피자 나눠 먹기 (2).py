def solution(M, N):
    answer = 0
    if M > 1:
        answer += M - 1
    if N > 1:
        answer += (N - 1) * M
    return answer


a = 1
b = 1
# c = 2
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
