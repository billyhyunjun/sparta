def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr2) > len(arr1):
        return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr2) > sum(arr1):
            return -1
        else:
            return 0



a = [49, 13]
b = [70, 11, 2]
# c = 3
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
print(result)