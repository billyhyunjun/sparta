def solution(answers):

    user1 = [1, 2, 3, 4, 5]
    user2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    point = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == user1[i%len(user1)]:
            point[0] += 1
        if answers[i] == user2[i%len(user2)]:
            point[1] += 1
        if answers[i] == user3[i%len(user3)]:
            point[2] += 1

    answer = []
    for i in range(len(point)):
        if point[i] == max(point):
            answer.append(i+1)
    return answer


a = [1,3,2,4,2]
result = solution(a)
print(result)