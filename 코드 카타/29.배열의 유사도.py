def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer
# -- 교집합을 이용항 방식--
# def solution(s1, s2):
#     return len(set(s1)&set(s2));

a = ["a", "b", "c"]
b = ["com", "b", "d", "p", "c"]
# c = 3
result = solution(a, b)
print(result)
