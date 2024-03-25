def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
    return arr


a = [4,3,2,1]
# b = 20
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)