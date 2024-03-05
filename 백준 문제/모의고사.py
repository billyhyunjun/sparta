def solution(answers):
    # 못난 학생 받아라
    user1 = [1, 2, 3, 4, 5]
    user2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 정답 맞춘 못난이1,2,3 정답 갯수
    point = [0, 0, 0]

    # 문제 총 갯수에 맞추어 반복하기
    for i in range(len(answers)):
        # 1번 못난이 맞춘 정답
        if answers[i] == user1[i%len(user1)]:
            point[0] += 1
        # 2번 못난이 맞춘 정답
        if answers[i] == user2[i%len(user2)]:
            point[1] += 1
        # 3번 못난이 맞춘 정답
        if answers[i] == user3[i%len(user3)]:
            point[2] += 1

    # 정답 순위 1위 받습니다. 공동 1등도 받습니다.
    answer = []
    # 정답자 한명씩 돌아서 최고 점수랑 같으면 1등 갑니다.
    for i in range(len(point)):
        if point[i] == max(point):
            answer.append(i+1)  # 0,1,2번 리스트니깐 1,2,3 몬난이 해줄려면 +1하자
    return answer


a = [1,3,2,4,2]
result = solution(a)
print(result)