# 값 입력
n = int(input())
c_time = []
for i in range(n):
    c_time.append(list(map(int, input().split())))

c_time.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in c_time:
    if end_time <= start:
        count += 1
        end_time = end

print(count)

