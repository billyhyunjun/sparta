import re


def solution(my_string):
    answer = 0
    c = re.findall(r'\d+', my_string)
    for i in c:
        answer += int(i)
    return answer

# re.findall: 정규 표현식 모듈인 re의 findall 함수를 호출합니다.
# 이 함수는 주어진 패턴에 매칭되는 모든 문자열을 찾아 리스트로 반환합니다.
#
# r'\d+': 이것은 정규 표현식 패턴입니다. \d는 숫자를 나타내는 메타 문자이며,
# +는 그 앞에 있는 문자나 문자 집합이 하나 이상 연속해서 나오는 것을 의미합니다.
# 따라서 \d+는 하나 이상의 숫자에 해당하는 문자열을 찾습니다.
#
# my_string: 이 부분은 찾고자 하는 문자열을 나타냅니다.
# 이 문자열에서 숫자를 찾아야 합니다.


a = "aAb1B2cC34oOp"
# b = 20
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
