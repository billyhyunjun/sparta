from itertools import permutations
# 횟수 입력
n = int(input())
# 번호 3개를 가지고 있는 사람들 모조리 가져오기  (여기서 123,124,125라는 번호를 받은 사람으로 취급한다.)
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# 반복문 진입 n번
for count in range(n):
    # 입력 받고 띄어쓰기 기준으로 test, strike, ball에 맞추어 넣기
    test, strike, ball = map(int, input().split())
    # 번호 모두 뜯어서 문자로 바꾸고 리스트에 넣기
    test = list(str(test))
    # 리스트 밀림 방지용!! 이건 이해가 필요하다
    remove_cnt = 0

    # 전체 사람 명단 모두 검사 받기
    for i in range(len(num)):
        # 새로운 명단 받고 볼 스트라이크 초기화
        s_cnt = b_cnt = 0
        # 리스트가 삭제가 되면 그만큼 뒤로 물려서 사용하기 위해서 뒤고가기 값을 만들었다고 생각하자.
        i -= remove_cnt

        # 각 숫자의 번호를 하나씩 꺼내서 비교하기 [1,2,3]이면 1번 꺼내서 비교!
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
        # 반복문을 통과 하고 나온 값이 볼 스트라이크와 일치하면 살려주고 값이 다르면 빼기
        if s_cnt != strike or b_cnt != ball:
            # 명단에서 빼기
            num.remove(num[i])
            # 명단이 비어 빈칸이 생긴만큼 뒤로가기 값 올려줘야지
            remove_cnt += 1
# 살아 남은 자의 수
print(len(num))
