# 사람 수 입력
n = int(input())
# 각 인원당 걸리는 시간
time = list(map(int, input().split()))

# 순서대로 배정
time.sort()
# 전체 값 합치는 곳
total_time = 0

# 앞에서 부터 i+1번쨰 까지 합치고 total_time에 입력
for i in range(len(time)):
    # for문 돌면서 한칸씩 앞으로!
    total_time += sum(time[:i+1])

print(total_time)