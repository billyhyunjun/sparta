# 10*10 색종이 만들기
def solution(x, y):
    # list 대신 집합을 이용 이것이 시간이 더 짧다.
    set_list = set()
    # x축10배 y축10배 생산
    for i in range(10):
        for j in range(10):
            # xy 좌표를 1씩 이동 시키면서 위치 값을 튜플형식으로 set에 저장 튜플 형식만 저장가능
            set_list.add((x + i, y + j))
    return set_list

# 입력값 받기
n = int(input())
# 합집합으로 겹치는 부분 제거하게 될 통
colored_paper = set()
# 색종이 갯수 만큼 반복 입력
for i in range(n):
    # 색종이 좌표값 띄어쓰기 기준으로 입력으로 나누어서 입력 받기
    paper = list(map(int, input().split()))
    # 기존의 색종이와 새로만든 색종이의 좌표값을 겹치지 않게 합집합으로 합치기
    colored_paper = (colored_paper | solution(paper[0], paper[1]))

print(len(colored_paper))