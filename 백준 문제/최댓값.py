for i in range(1, 10):
    # 1번 줄부터 9번 줄까지 쭉 받아서 리스트에 넣기
    globals()["line{}".format(i)] = list(map(int, input().split()))
    # 리스트중에서 최고 값을 뽑아서 변수 만들기
    globals()["max_line{}".format(i)] = max(globals()['line{}'.format(i)])

# 만들어진 max 값 리스트에 넣어서 한 줄로 만들기
max_max = []
for i in range(1, 10):
    max_max.append(globals()['max_line{}'.format(i)])

# 그중에 또 최고 값 찾기
first_value = max(max_max)
print(first_value)
# 반복문 탈출용 플레그
flag = False
# 최고 값을 찾았으니 최고 값이 위치하고 있는 좌표 값 찾기
for i in range(1, 10):
    # 만약에 최고 값이 그라인중에 최고 값이랑 동일 하다면 반복문 진입
    if globals()['max_line{}'.format(i)] == first_value:
        # 여기서는 기존의 라인[21 77 45 35 28 75 90 76 1] 중에서 최고 값이 있는 위치 찾기
        for j in range(1, 10):
            # 리스트는 0 부터 시작이고 우리가 아는 좌표는 1부터 시작이니 -1 이든 +1이든 달아주어야함
            if globals()['line{}'.format(i)][j - 1] == first_value:
                # 좌표 위치 표시
                print(f"{i} {j}")
                # 답을 찾았으니 플래그 온!
                flag = True
                break
    # 플래그가 참이면 탈출!
    if flag:
        break
