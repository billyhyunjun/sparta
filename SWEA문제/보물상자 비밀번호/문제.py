import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


# 문자 회전 시키는 함수
def text_rotate(text):
    one_text = text[0]
    remove_text = text[1:]
    sum_text = remove_text + one_text
    return sum_text


# 각 문자에 맞추어 16진수 비밀번호 만들기
def make_hex(text, num):
    # 16진수 받을 통
    text_list = []
    # 반복 제한 한 변이 돌면 끝
    n = 0
    # 반복 시작
    while n < num:
        # num글자 마다 때야 하니깐 num씩 증가 마지막은 num - 1만큼은 필요 없음
        for i in range(0, len(text) - num + 1, num):
            # 만든 번호가 저장되어 있지않다면 넣기
            if text[i:i + num] not in text_list:
                text_list.append(text[i:i + num])
        #  문자 돌리기
        text = text_rotate(text)
        # 한 칸씩 앞으로
        n += 1
    return text_list


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # n // 4 해주면 글자수가 만들어짐
    n, k = map(int, input().split())
    # 문자 그대로 받아주기
    x = input()
    # 16진수를 10진수로 변환해서 옴겨 담기
    pass_word = []
    for i in make_hex(x, n // 4):
        pass_word.append(int(i, 16))
    # 10진수 정렬
    pass_word.sort(reverse=True)
    # 출력
    print(f"#{test_case} {pass_word[k-1]}")