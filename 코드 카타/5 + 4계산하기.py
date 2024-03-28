def solution(my_string):
    answer = 0
    string = my_string.split()
    flag = True
    for i in string:
        if i == "+":
            flag = True
        elif i == "-":
            flag = False
        else:
            if flag:
                answer += int(i)
            else:
                answer -= int(i)
    return answer

# solution = eval

a = "3 + 40"
# b = 5
# c = 4
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)

