import sys
from collections import deque

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 각각 트력의 개수, 다리 길이, 최대 가능 무게
n, w, l = map(int, input().split())

# 트럭 순서 및 다리 위에 올라간 트럭 순서 표기
queue_b = deque()
queue_t = deque()

# 다리위에 올라간 트럭 표시
for _ in range(w):
    queue_b.append(0)
# 올라갈 트럭을 나누어서 큐에 입력
for i in list(map(int, input().split())):
    queue_t.append(i)

# 시간 측정
counter = 0

# 대기중인 모든 트럭이 출발하면 종료
while len(queue_t) > 0:
    # 횟수 1회 증가
    counter += 1
    # 다리 위에 트럭의 총 무게가 다리 최대 가능 무게를 넘기지 않는가? + 마지막으로 빠지는 트럭은 계산에 넣지 않는다.
    if sum(queue_b) - queue_b[0] + queue_t[0] <= l:
        # 0번 트럭 아웃
        queue_b.popleft()
        # 대기 트럭 0번 빼서 다리 마지막 줄에 추가
        queue_b.append(queue_t.popleft())
    else:
        # 다리 가능 무게 다차면 다리위에 트럭만 전진하고 빈공간 하나 채우기
        queue_b.popleft()
        queue_b.append(0)

# 마지막 대리열 트럭이 다리위에 올라갔다면 이제는 마지막트럭이 다리만 지나가면 되니 다리길이인 w만 추가 하면 된다.
print(counter + w)
