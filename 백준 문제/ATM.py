# 값 입력
n = int(input())
time = list(map(int, input().split()))

# 순서대로 배정
time.sort()

total_time = 0

# 앞에서 부터 i+1번쨰 까지 합치고 total_time에 입력
for i in range(len(time)):
    total_time += sum(time[:i+1])

print(total_time)