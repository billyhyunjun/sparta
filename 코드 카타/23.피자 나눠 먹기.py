def solution(n):
    if divmod(n, 7)[1] > 0:
        answer = divmod(n, 7)[0] + 1
    else:
        answer = divmod(n, 7)[0]
    return answer


a = 15
# b = "f"
# c = 3
result = solution(a)
print(result)
