def solution(s):
    answer = []
    flag = True
    for i in s:
        if i == " ":
            answer.append(i)
            flag = True
        else:
            if flag:
                answer.append(i.upper())
                flag = False
            else:
                answer.append(i.lower())
                flag = False
    return "".join(answer)


# 내장 함수
# def solution(s):
#     # 함수를 완성하세요
#     return s.title()


a = "  for the what 1what  "
# b = 2
# c = 20
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
