def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1


def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]


a = [[1], [2]]
b = [[3], [4]]
# c = 20
# d = 50
# result = solution(a)
result = sumMatrix(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
for x in zip(a, b):  # [([1], [3]), ([2], [4])]
    print(x) # ([1], [3])
    print(*x) # [1] [3]
    print(list(zip(*x))) # [(1, 3)]
    print(list(map(sum, zip(*x)))) # [4]
