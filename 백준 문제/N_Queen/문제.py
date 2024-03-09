import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


# 내가 놓는 자리가 퀸의 공격 범위 안에 있는가?
def solve(x):
    # y축 = i 돌면서 x의 값이 1이 있는 지를 검사 하는 것  row[x] == row[i]는 가로축 검사 abs(row[x] - row[i]) == abs(x - i)는 대각선 검사
    for i in range(x):
        # abs(x - i) 이거는 x와 i 간의 절대값 차이를 나타 내는 것이다 -1 => 1
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


n = int(input())
counter = 0
row = [0] * n


def n_queen(x):
    global counter
    # 말 갯수가 다차면 끝
    if x == n:
        counter += 1
        return
    # 반복문 진행 하면서 x = [0], row[x] = [0] 부터 [n],[n]까지 하는 방법 이거는 좀 신기 하다...
    # 이 부분을 이해 할려면 row = [0], [1], [2], [3], [4], [5], [6], [7] 이렇게 있다면 한 칸씩은 x 축이 이고
    # 칸마다 들어가 있는 숫자가 y 축의 위치 라고 인식을 해야 한다... 이거 생각한 사람 천재..
    # y = [0] 부터 시작
    for i in range(n):
        # [x].[i]에 퀸 두기
        row[x] = i
        # 퀸 가능 여부
        if solve(x):
            # 가능 하면 다음 x 칸 진행!
            n_queen(x + 1)

    # 내가 처음 생각 한 방식의 문제는 재귀 함수를 처음 돌 때에는 문제가 없지만
    # [0]. [1]에 퀸을 둘 때 문제가 생겨서 그 부분을 해결 하지 못했다.

# x = [0] 부터 시작!
n_queen(0)
print(counter)

















# def create_matrix(num):
#     matrix = []
#     for i in range(num):
#         row = []
#         for j in range(num):
#             row.append(0)
#         matrix.append(row)
#     return matrix
#
# def clear_matrix(num):
#     global board
#     matrix = []
#     for i in range(num):
#         row = []
#         for j in range(num):
#             board[i][j] = 0
#         matrix.append(row)
#     return matrix
#
#
# def reverse_board(x, y, num):
#     global board
#     for i in range(num):
#         board[x][i] = 1
#         board[i][y] = 1
#     for i in range(num):
#         if 0 <= x - i < num and 0 <= y - i < num:
#             board[x - i][y - i] = 1
#         if 0 <= x + i < num and 0 <= y + i < num:
#             board[x + i][y + i] = 1
#         if 0 <= x - i < num and 0 <= y + i < num:
#             board[x - i][y + i] = 1
#         if 0 <= x + i < num and 0 <= y - i < num:
#             board[x + i][y - i] = 1
#
#
# def n_queen(item, num):
#     global counter
#     global board
#     if item == num:
#         counter += 1
#         clear_matrix(num)
#         return
#     for x in range(num):
#         if x >= item:
#             for y in range(num):
#                 if board[x][y] == 1:
#                     pass
#                 else:
#                     reverse_board(x, y, num)
#                     n_queen(item + 1, num)
#
#
# n = int(input())
# counter = 0
# # board[x][y]
# board = create_matrix(n)
# n_queen(0, n)
# print(counter)