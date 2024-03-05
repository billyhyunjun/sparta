def solution(num_list):
    answer = []
    for num in reversed(num_list):
        answer.append(num)
    return answer


a = [1, 2, 3, 4, 5]

result = solution(a)
print(result)
