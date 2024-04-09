def solution(s):
    answer = [i for i in s]
    c = 0
    z = 0
    while answer != ["1"]:
        z += answer.count("0")
        c += 1
        answer = [x for x in answer if x != "0"]
        answer = [i for i in bin(len(answer))[2:]]
    return [c, z]
#
# def solution(s):
#     a, b = 0, 0
#     while s != '1':
#         a += 1
#         num = s.count('1')
#         b += len(s) - num
#         s = bin(num)[2:]
#     return [a, b]


a = "01110"
# b = ["sod", "eocd", "qixm", "adio", "soo"]
# c = 2
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
