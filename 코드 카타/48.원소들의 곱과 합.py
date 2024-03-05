def solution(num_list):
    multiply = 1
    for i in num_list:
        multiply *= i
    sum_square = (sum(num_list) ** 2)
    if sum_square < multiply:
        answer = 0
    else:
        answer = 1
    return answer


a = [3, 4, 5, 2, 1]
# b = 7
# c = True
result = solution(a)
print(result)