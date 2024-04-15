def solution(score):
    answer = [0]*len(score)
    rank = [sum(i)/len(i) for i in score]
    sorted_rank = sorted(rank, reverse=True)
    for i, x in enumerate(sorted_rank):
        for j, y in enumerate(rank):
            if x == y and answer[j] == 0:
                answer[j] = i + 1
    return answer

a = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
# b = [False, True, True, True, True, False, False]
# c = 2
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
