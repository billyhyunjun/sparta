def solution(array):
    list = sorted(array)
    answer = list[len(list)//2]
    return answer


a = [1, 2, 7, 10, 11]
# b = 10
# c = 3
result = solution(a)
print(result)
