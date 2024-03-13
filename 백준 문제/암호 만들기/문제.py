import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def back_tracking(cnt, idx):
    # l글자 만큼 만들어진 문자 모음 자음 갯수 확인
    if cnt == l:

        vo, co = 0, 0
        # 4개의 문자 수의 맞추어
        for i in range(cnt):
            if check_list[i] in vowel:
                vo += 1
            else:
                co += 1
        # 자음 모음 조건에 맞추어 들어 갔으면 실행
        if vo >= 1 and co >= 2:
            print("".join(check_list))

        return

    # 0번 부터 6번 까지의 문자 하나씩 빼서 넣기
    for i in range(idx, c):
        # 해당 위치 문자 입력
        check_list.append(words[i])
        # i번째 입력 했으니 다음 문자 입력
        back_tracking(cnt + 1, i + 1)
        # i번째 다썻으면 다음 i+1번째 넣고 다시 반복문 실행
        check_list.pop()


l, c = map(int, input().split())
words = sorted(list(input().split()))

vowel = ['a', 'e', 'i', 'o', 'u']
check_list = []
back_tracking(0, 0)











# import itertools
#
#
# l, c = map(int, input().split())
# list_consonant = sorted(list(input().split()))
# list_vowel = []
# for i, char in enumerate(list_consonant):
#     if char in ["a", "e", "i", "o", "u"]:
#         list_vowel.append(list_consonant.pop(i))
# answer = []
#
#
# def make_list(vow, con):
#     if vow < 1:
#         return
#
#     vowel = list(itertools.combinations(list_vowel, vow))
#     consonant = list(itertools.combinations(list_consonant, con))
#     if con >= 2:
#         for i in vowel:
#             for j in consonant:
#                 answer.append("".join(sorted(i + j)))
#
#     make_list(vow - 1, con + 1)
#
#
# make_list(l, 0)
# for i in sorted(answer):
#     print(i)
