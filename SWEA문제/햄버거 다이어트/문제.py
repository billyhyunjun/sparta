import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 횟수 받기
    num, cal = map(int, input().split())
    # 맛잇는 통
    t = []
    # 칼로리 통
    k = []

    # 가능한 햄버거를 찾는 기계?
    def dfs(i, taste, kcal):
        # 최고 기록 가져 가기
        global max_taste
        # 맛있게 만든 버거 라도 칼로리가 높으면 out!
        if kcal > cal:  # 칼로리 초과
            return
        # 칼로리도 넘지 않고 재료도 한번 씩 썻다면 최고의 음식
        if taste > max_taste:  # 최대 칼로리 저장
            max_taste = taste
        # 재료의 갯수가 넘어 가도 out!
        if i == num:  # 끝
            return
        # 재료를 선택 할지 말지를 고르는 선택지
        # i번 째에 있는 재료를 사용 한다! 그리고 그 만큼 맛과 칼로리도 챙겨가
        dfs(i + 1, taste + t[i], kcal + k[i])
        # 모든 재료로 비교를 다 해봐서 재료 수를 넘겨서 다른 방법을 찾거나 칼로리의 양이 넘어가 버려서 아웃 되어 버렸으니 패스 하는 것
        dfs(i + 1, taste, kcal)

    # 재료 갯수 만큼 칼로리랑 맛 기록하기
    for _ in range(num):
        tasty, cals = map(int, input().split())
        t.append(tasty)
        k.append(cals)

    # 최고 기록을 만들자
    max_taste = 0
    # 이제 재료 들을 넣고 햄버거를 만들어 보자 먼저 아무 것도 안했을 때에 칼로리랑 맛부터
    dfs(0, 0, 0)
    # 출력!
    print(f'#{test_case} {max_taste}')


# ----실패한 나의 작품----
# from itertools import combinations


# def low_cal(list_x, max_cals):
#     pass_buggers = []
#     for z in range(1, len(list_x) + 1):
#         if z == 1:
#             for m in list_x:
#                 if m[1] <= max_cals:
#                     pass_buggers.append(m)
#         else:
#             buggers = combinations(list_x, z)
#             for j in buggers:
#                 sum_cal = [sublist[1] for sublist in j]
#                 if sum(sum_cal) <= max_cals:
#                     pass_buggers.append(j)
#     return pass_buggers
#
#
# def max_tasty(list_bugger):
#     max_taste = 0
#     for x in list_bugger:
#         sum_tasty = 0
#         if isinstance(x, list):
#             sum_tasty += x[0]
#         else:
#             for j in x:
#                 sum_tasty += j[0]
#         if sum_tasty > max_taste:
#             max_taste = sum_tasty
#     return max_taste
#
#
# T = int(input())
# # 여러 개의 테스트 케이스 가 주어 지므로, 각각을 처리 합니다.
# for test_case in range(1, T + 1):
#     num, max_cal = map(int, input().split())
#     items = []
#
#     for i in range(num):
#         items.append(list(map(int, input().split())))
#
#     eat_able_bugger = low_cal(items, max_cal)
#     most_bugger = max_tasty(eat_able_bugger)
#
#     print(f"#{test_case} {most_bugger}")
