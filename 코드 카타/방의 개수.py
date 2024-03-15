from collections import defaultdict


def solution(arrows):
    # 좌표 이동 방법 [0,1,2,3,4,5,6,7]
    move = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    # 맨 처음 시작할 위치 (defaultdict 딕셔너리에 리스트를 넣을 때에는 튜플로 넣어야 합니다.)
    position = (0, 0)
    # 만들어진 방의 개수
    counter = 0
    # 방문자 {점위치 : [(x,y),(x,y),(x,y),(x,y)]} <- 이어진 점들
    visit = defaultdict(list)
    # 각 이동에 맞추어 점 이동
    for arrow in arrows:
        # 대각선을 위해서 크기를 2배로 키워준다.
        for _ in range(2):
            # 이동할 점 위치 표시
            move_position = (position[0] + move[arrow][0], position[1] + move[arrow][1])
            # 방문자 명단에서 방문한 점(key)일 경우와 방문은 했지만 해당 방향으로 입장(value)은 처음인 경우
            if move_position in visit and move_position not in visit[position]:
                # 방 한개 완성
                counter += 1
                # 출발하기 전 점과 이동한 점을 서로 연결을 시켜준다.
                visit[position].append(move_position)
                visit[move_position].append(position)
            # 방문을 기록이 없는 처음 찍는 점일 경우
            elif move_position not in visit:
                # 출발하기 전 점과 이동한 점을 서로 연결을 시켜준다.
                visit[position].append(move_position)
                visit[move_position].append(position)
            # 2배로 이동을 해야 하니 이동한 점을 출발점으로 넣어준다
            position = move_position
    # 만들어진 방 출력
    return counter


a = [6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]
# b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# c = 3
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
print(result)

# ---구글링 도움--
# from collections import defaultdict
# def solution(arrows):
#     answer = 0
#     visit = defaultdict(list)
#     x,y = 0,0
#     dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
#
#     for arrow in arrows:
#         for _ in range(2):              # 대각선 판별을 위해 2씩
#             nx = x + dx[arrow]
#             ny = y + dy[arrow]
#             if (nx,ny) in visit and (x,y) not in visit[(nx,ny)]:    # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
#                 answer += 1
#                 visit[(x,y)].append((nx,ny))
#                 visit[(nx,ny)].append((x,y))
#             elif (nx,ny) not in visit:                  # 방문하지 않았던 경우
#                 visit[(x,y)].append((nx,ny))            # 경로가 겹치는 경우는 따로 해줄 필요 없음
#                 visit[(nx,ny)].append((x,y))
#             x,y = nx, ny        # 이동
#     return answer

# --- 처음만들었던 방법 반례사례가 너무 많아서 실패----
# def solution(arrows):
#     dot = []
#     move = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
#     position = [0, 0]
#     dot.append(position)
#     for arrow in arrows:
#         position = [position[0] + move[arrow][0], position[1] + move[arrow][1]]
#         if position not in dot:
#             dot.append(position)
#
#     return (len(arrows)-len(dot))+1
#
#
# a = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
# # b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# # c = 3
# result = solution(a)
# # result = solution(a, b)
# # result = solution(a, b, c)
# print(result)
