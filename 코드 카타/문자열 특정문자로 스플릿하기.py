import re


def solution(myStr):
    answer = re.split("[abc]", myStr)
    answer = list(filter(None, answer))
    if not answer:
        answer.append('EMPTY')
    return answer


a = "baconlettucetomato"
# b = 20
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)