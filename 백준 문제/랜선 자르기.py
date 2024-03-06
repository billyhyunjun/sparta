# k와 n값 입력
k, n = map(int, input().split())
# n개 나올 수 있는 길이
answer = 0
# k개 라인 종류 받아오기
line = []
# k번 길이 입력
for i in range(k):
    line.append(int(input()))
# k개 랜선 중에 가장 긴 라인 찾기
line_max = max(line)

# 라인 찾는 함수
def binary(low, high):
    # 최고 길이가 최저 길이 보다 작아 졌을 때 기저 사례~!
    if high <= low:
        return
    # 함수 밖에 변수를 가져올 때 사용
    global n
    global answer
    # 함수가 시작이 되면 가능한 범위 에서 가장 큰 값과 작은 값의 반이 되는 길이를 정함
    mid = (low + high) // 2
    # n개가 될 수 있는지 검사를 위해서 빈통 준비
    temp = 0
    # k개의 라인을 돌면서 하나 씩 mid 의 길이로 잘라 본다.
    for item in line:
        # 자르고 나서 생기는 라인의 갯수를 temp 에 저장
        temp += item // mid
    # 만약에 우리가 원하는 n개의 라인을 만들 수 있다면 그 길이를 answer 에 저장 한다.
    if temp >= n:
        answer = mid
        # 값을 찾았으니 빠져 나가기 위해서 low 에 mid+1 값을 넣고 돌리면 다음 함수가 한 바퀴를 돌 때 맨 처음 if 으로 인해서 나갈 수 있음
        binary(mid + 1, high)
    else:
        # 이 값 으로는 n개를 만들 수 없기 때문에 중앙 값을 high 로 잡고 다시 해보자.
        binary(low, mid - 1)


binary(0, line_max * 2)
print(answer)
