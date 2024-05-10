# def solution(sizes):
#     answer = 0
#     # 첫 번째 서브 리스트를 두 번째 요소에 따라 정렬
#     for i in range(len(sizes)):
#         sizes[i].sort()
#     sort_list = sorted(sizes, key=lambda x: x[0], reverse=True)
#     row = sort_list[0][0]
#     sort_list = sorted(sizes, key=lambda x: x[1], reverse=True)
#     column = sort_list[0][1]
#     return row*column

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


a = [[60, 50], [30, 70], [60, 30], [80, 40]]
# b = [[1,2]]
# c = 20
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
