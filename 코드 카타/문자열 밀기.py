def solution(A, B):
    answer = 0
    while True:
        if A == B:
            break
        if answer == len(A):
            answer = -1
            break
        A = A[-1] + A[:-1]
        answer += 1
    return answer

# solution=lambda a,b:(b*2).find(a)

a = "hello"
b = "ohell"
# c = 20
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
