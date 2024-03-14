import heapq
import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 힙통
    heap = []
    # 출력 받아올 pop 밥통
    text = []
    # 실행 횟수
    n = int(input())
    # 반복문 실행
    for _ in range(n):
        # 넣는거면 1,2 두개로 들어오고 뺴는 거면 2 만 만들어옴
        a = list(map(int, input().split()))
        # 그러므로 글자수가 2개면 넣는 방향으로
        if len(a) > 1:
            heapq.heappush(heap, -a[1])
        #  글자수가 1개이면 빼는 방향으로
        else:
            # 그중에서도 힙통이 비면 뺄게 없으니 -1이라도 출력
            if len(heap) == 0:
                text.append(-1)
            else:
                # 출력할게 있으면 가장 큰 숫자 빼내기 (-로 넣고 빼고 -하면 큰값이 됩니다.)
                text.append(-heapq.heappop(heap))
    # 모아놓은 출력 상자 뽑아서 문자로 만들기
    t = " ".join(map(str, text))
    print(f"#{test_case} {t}")


# ---- 다른 방법 ---
# MAXN = 100000
#
# heap = [0] * MAXN
# heapCnt = 0
#
# def add(val):
#     global heapCnt
#     pivot = heapCnt
#     heap[heapCnt] = val
#     heapCnt += 1
#     while pivot > 0:
#         ppivot = pivot
#         pivot -= 1
#         pivot //= 2
#         if heap[pivot] < val:
#             heap[ppivot] = heap[pivot]
#             heap[pivot] = val
#         else:
#             return
#
# def pop():
#     global heapCnt
#     if heapCnt == 0:
#         return -1
#     val = heap[0]
#     heapCnt -= 1
#     heap[0] = heap[heapCnt]
#     pivot = 0
#     while True:
#         ppivot = pivot
#         pivot *= 2
#         pivot += 1
#         if pivot >= heapCnt:
#             break
#         elif pivot + 1 == heapCnt:
#             if heap[ppivot] > heap[pivot]:
#                 break
#             tmp = heap[ppivot]
#             heap[ppivot] = heap[pivot]
#             heap[pivot] = tmp
#             break
#         else:
#             if heap[pivot] < heap[pivot + 1]:
#                 pivot += 1
#             if heap[ppivot] > heap[pivot]:
#                 break
#             tmp = heap[pivot]
#             heap[pivot] = heap[ppivot]
#             heap[ppivot] = tmp
#     return val
#
# T = int(input())
# for tc in range(1, T + 1):
#     print('#' + str(tc), end=' ')
#     heapCnt = 0
#     N = int(input())
#     for _ in range(N):
#         act = list(map(int, input().split()))
#         if act[0] == 1:
#             num = act[1]
#             add(num)
#         else:
#             print(pop(), end=' ')
#     print()




