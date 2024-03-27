def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        num_list = []
        for j in range(1,i+1):
            if i % j == 0:
                num_list.append(j)
        if len(num_list) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer

a = 13
b = 17
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# d = True
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)