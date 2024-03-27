def solution(arr):
    answer = 0
    num_list = arr[:]
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = (arr[i] * 2) + 1

        if arr == num_list:
            return answer
        else:
            num_list = arr[:]
            answer += 1

# def solution(arr):
#     answer = 0
#     old = arr
#     while(True):
#         new = []
#         for i in old:
#             if i>=50 and i%2 == 0:
#                 i = i/2
#             elif i<50 and i%2 == 1:
#                 i = i*2 + 1
#             new.append(int(i))
#         if old == new:
#             break
#         else:
#             old = new
#             answer += 1
#     return answer


a = [1, 2, 3, 100, 99, 98]
# b = "11"
# c = "qjnwezgrpirldywt"
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
