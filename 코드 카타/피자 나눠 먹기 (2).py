def solution(spell, dic):
    for word in dic:
        counter = 0
        for a in spell:
            if a in word:
                counter += 1
            if counter == len(spell):
                return 1
    return 2


# def solution(spell, dic):
#     spell = set(spell)
#     for s in dic:
#         print(len(spell) == len(s))
#         if not spell-set(s):
#             if (len(spell) == len(s)) and (not spell - set(s)):
#                 return 1
#     return 2


a = ["p", "o", "s"]
b = ["sod", "eocd", "qixm", "adio", "soo"]
# c = 2
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
