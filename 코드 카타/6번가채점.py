def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer


a = [1]
b = [100]
c = [100, 80, 90, 84, 20]
# d = 50
# result = solution(a)
# result = solution(a, b)
result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
