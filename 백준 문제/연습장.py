# num = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 4, 3],[1, 4, 3]]
# test = 4
#
# print(num[0].index(test))
#
# # 시간 표시
# import math
# import time
#
# start = time.time()
# math.factorial(100000)
# end = time.time()
#
# print(f"{end - start:.5f} sec")
import time


# found_text = ['a', 'b', 'b', 'a', 'b', 'a', 'a', 'b']
#
# print(found_text == list)

# n = 7
# x = n // 2
#
# for j in range(len(found_text) - n):
#     var = found_text[j:j + x] == found_text[j + x + 1: j + (x * 2) + 1][::-1]
#     print(found_text[j:j + x])
#     print(found_text[j + x + 1: j + (x * 2) + 1][::-1])
#     print(var)


# for Count in range(10):
#     N = int(input())
#     List = list(input() for _ in range(8))
#     Answer = 0
#
#     # 가로 확인
#     for y in range(8):
#         for x in range(8 - N + 1):
#             A = List[y][x:x + N]
#             if A == A[::-1]:
#                 Answer += 1
#
#     # 세로 확인
#     for y in range(8 - N + 1):
#         for x in range(8):
#             A = ''
#             for z in range(N):
#                 A += List[y + z][x]
#             if A == A[::-1]:
#                 Answer += 1
#     print("#{} {}".format(Count + 1, Answer))


#
# # 입력 리스트
# input_list = ([100, 200], [300, 500])
#
# print(len(input_list))
# my_dict = {}
# my_dict["key","a","b"] = [100, 200, 300]
# print(my_dict)
#
# a = [1, 4]
# b = [[1, 4], [1, 2]]
# print(a not in b)
#
# a = 1
# b = 0
# print(f"{a}{b}" in ['00', '10', '20', '30', '20', '30'])

# a = "1234"
# a.

def power(a, b):
    if b == 0:
        return 1

    x = power(a, b // 2)

    if b % 2 == 0:
        return x * x

    else:
        return x * x * a


start = time.time()
a = 2 ** 2000000000
# power(2, 2000000000)
end = time.time()
print(end - start)