def solution(slice, n):
    if divmod(n, slice)[1] > 0:
        answer = divmod(n, slice)[0] + 1
    else:
        answer = divmod(n, slice)[0]
    return answer


a = 4
b = 12
# c = 3
result = solution(a, b)
print(result)
