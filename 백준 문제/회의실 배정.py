# 회의 갯수
n = int(input())
# 회의 시작 끝 리스트 명단
c_time = []
# 회의 갯수 만큼 시간표 받아오기
for i in range(n):
    # 띄어쓰기 기준으로 [시작, 끝] 리스트 생성 후 회의 명단에 넣기
    c_time.append(list(map(int, input().split())))

# 이거는 각 리스트의 [1]번째 리스트 값을 기준으로 오름차순 정렬을 하고 [1]번값이 같을때에는 [2]번을 기준으로 오름차순
c_time.sort(key=lambda x: (x[1], x[0]))

# 회의 개최 횟수
count = 0
# 최근에 끝난 회의 시간
end_time = 0

# 반복문 돌면서 회의끝난 시간이 빠른 순으로 회의 시작 끝 대입
for start, end in c_time:
    # 최근의 끝난 회의를 기준으로 시작시간이 같거나 이후라면 회의 시작합시다
    if end_time <= start:
        count += 1 # 회의 개최 !
        end_time = end # 끝나는 시간 입력

print(count)

