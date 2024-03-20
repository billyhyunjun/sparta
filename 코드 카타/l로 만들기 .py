def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer


a = "banana"
# b = [[1, 3], [0, 4]]
# c = 2
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
print(result)
