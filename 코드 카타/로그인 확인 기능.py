def solution(id_pw, db):
    answer = ''
    id_list = [i[0] for i in db]
    if id_pw[0] not in id_list:
        answer = "fail"
    elif id_pw[1] != db[id_list.index(id_pw[0])][1]:
        answer = "wrong pw"
    else:
        answer = "login"
    return answer


a = ["rabbit04", "1234"]
b = [["rabbit04", "98761"], ["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "rabbit04"]]
# c = 2
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
