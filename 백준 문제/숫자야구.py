from itertools import permutations
# 횟수 입력
n = int(input())
# 번호 3개를 가지고 있는 사람들 모조리 가져오기
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# 반복문 진입 n번
for count in range(n):
    # 숫자 입력 받기
    test, strike, ball = map(int, input().split())
    # 번호 모두 뜯어서 문자로 바꾸고 리스트에 넣기
    test = list(str(test))
    # 리스트 오류 방지용
    remove_cnt = 0

    # 전체 사람 명단 모두 검사 받기
    for i in range(len(num)):
        # 볼 스트라이크 초기화
        s_cnt = b_cnt = 0
        # 리스트가 삭제가 되면 그만큼 뒤로 물려서 사용하기 위해서
        i -= remove_cnt

        # 각 숫자의 번호를 하나씩
        for j in range(3):
            # 문자로 바뀐 번호를 다시 숫자로 바꾸기
            test[j] = int(test[j])
            # 내가 적은 번호 j번 자리가 3자리 번호안에 있는지?
            if test[j] in num[i]:
                # 있다면 3자리 안에 있으면서도 j번 째의 자리가 목록에서 가져온 것에도 j번째 자리에 있는가? 있으면 스트라이크
                if j == num[i].index(test[j]):
                    s_cnt += 1
                # 같은 자리는 아니라면 볼
                else:
                    b_cnt += 1
        # 반복문을 통과 하고 나온 값이 볼 스트라이크와 일치하면 살여주기 다르면 죽이기
        if s_cnt != strike or b_cnt != ball:
            # 죽여
            num.remove(num[i])
            # 죽여 버렸으니 빈칸을 다시 뒤로 돌려야지
            remove_cnt += 1
# 살아 남은 자의 수
print(len(num))
