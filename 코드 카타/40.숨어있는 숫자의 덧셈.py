def solution(my_string):
    answer = 0
    for i in my_string:
        if i in '0123456789':
            answer += int(i)
    return answer

a = "aAb1B2cC34oOp"
# b = 3
# c = 3
result = solution(a)
print(result)
