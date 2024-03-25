def solution(arr):
    i = 1
    while i < len(arr):
        i *= 2
    answer = [0]*i
    for j in range(len(arr)):
        answer[j] = arr[j]
    return answer


a = [1, 2, 3, 4, 5, 6]
# b = 20
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)