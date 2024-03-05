def solution(num_list):
    odd = ""
    even = ""
    for i in num_list:
        if i % 2 == 0:
            odd += str(i)
        else:
            even += str(i)
    answer = int(odd) + int(even)
    return answer

a = [3, 4, 5, 2, 1]
# b = 11
# c = 3
result = solution(a)
print(result)
