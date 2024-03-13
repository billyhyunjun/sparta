import sys
from collections import deque

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 라우터가 최대로 담을 수 있는 정보의 크기
n = int(input())
# 데이터를 담을 큐의 통
queue = deque()
# -1이 나올 때까지 계속 반복문 진행
while True:
    # 입력값 받기
    input_x = int(input())
    # -1이면 반복문 종료
    if input_x == -1:
        break
    # 0 이면 큐에 있는 맨앞의 값 제거
    if input_x == 0:
        queue.popleft()
    # 0이 아니면서 큐가 가득차지 않았다면 새로운 값 받아주기
    else:
        if len(queue) < n:
            queue.append(input_x)

# 라우터가 비었으면 empty
if len(queue) == 0:
    print("empty")
# 정보가 있다면 정보 표시 *붙이면 가능하다.
else:
    print(*queue)

