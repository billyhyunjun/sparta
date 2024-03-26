# def solution(strArr):
#     answer = [[] for _ in range(max(len(s) for s in strArr) + 1)]
#     for i in strArr:
#         answer[len(i)].append(i)
#     return max(len(s) for s in answer)

# 딕셔너리
def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1
    print(d)
    return max(d.values())

a = ["a","bc","d","efg","hi"]
# b = [-3,-1,0,2]
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)