import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

from collections import deque

num = int(input())
queue = deque()
for i in range(1, num + 1):
    queue.append(i)


def card_shuffle(card):
    while len(queue) > 1:
        card.popleft()

        card.append(card.popleft())
    return card[0]


print(card_shuffle(queue))

# ---- 재귀 방식 -----


# from collections import deque
#
# num = int(input())
# queue = deque()
# for i in range(1, num + 1):
#     queue.append(i)
#
#
# def card_shuffle(card):
#     if len(card) == 1:
#         return card[0]
#     card.popleft()
#
#     card.append(card.popleft())
#     return card_shuffle(card)
#
#
# print(card_shuffle(queue))