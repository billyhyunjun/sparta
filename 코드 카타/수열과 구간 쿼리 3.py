def solution(arr, queries):
    for q in queries:
        x = arr[q[0]]
        arr[q[0]] = arr[q[1]]
        arr[q[1]] = x
    return arr
# def solution(arr, queries):
#     for a,b in queries:
#         arr[a],arr[b]=arr[b],arr[a]
#     return arr


a = [0, 1, 2, 3, 4]
b = [[0, 3],[1, 2],[1, 4]]
# c = 5
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
print(result)
