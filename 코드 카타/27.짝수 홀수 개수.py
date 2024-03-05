def solution(num_list):
    answer = [0, 0]
    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer


a = [1, 2, 3, 4, 5]
# b = 12
# c = 3
result = solution(a)
print(result)
