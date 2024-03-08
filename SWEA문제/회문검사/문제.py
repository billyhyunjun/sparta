import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def list_odd(list_num, share):
    if list_num[: share] == list_num[share: share * 2][::-1]:
        return 1
    else:
        return 0


def list_even(list_num, share):
    if list_num[: share] == list_num[share + 1: (share * 2) + 1][::-1]:
        return 1
    else:
        return 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    text = input()
    text_len = len(text)
    share_text = text_len // 2
    remain_text = text_len % 2
    list_text = list(text)

    # 짝수
    if remain_text == 0:
        print(f"#{test_case} {list_odd(list_text, share_text)}")

    # 홀수
    else:
        print(f"#{test_case} {list_even(list_text, share_text)}")



