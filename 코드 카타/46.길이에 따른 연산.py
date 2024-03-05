def solution(num_list):
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        answer = 1
        for num in num_list:
            answer *= num
    return answer


a = [2, 3, 4, 5]
# b = 7
# c = True
result = solution(a)
print(result)
