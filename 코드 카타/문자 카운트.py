def solution(s):
    answer = ''
    c = ''
    b = ''
    for i in s:
        if i not in b:
            b += i
        else:
            c += i
    for i in s:
        if i not in c:
            answer += i
    answer = sorted(answer)
    return "".join(answer)


# def solution(s):
#     answer = ''
#     for c in s:
#         if s.count(c) == 1:
#             answer += c
#     answer = ''.join(sorted(answer))
#     return answer

a = "abcabcadc"
# b = 20
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
