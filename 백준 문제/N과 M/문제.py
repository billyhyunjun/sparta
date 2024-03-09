import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def solve(list_num):
    # 변하지 않을 변수니깐 글로벌로 가져오기
    global m
    global n_list
    # 글자 수 가 같으면 출력
    if m == len(list_num):
        # 이거 잘보고 해야한다. 앞에서 숫자로 리스트에 넣었기 때문에 다시 글자로 바꾸어 주어야함 이번 같은 경우는 그냥 처음부터 문자로 해도됨
        print(" ".join(map(str, list_num)))
        return
    # 중복 검열
    for i in n_list:
        # 안에 있으면 패스
        if i in list_num:
            pass
        # 없으면 요인 추가 시켜서 재귀 참고로 append안된다.
        else:
            solve(list_num + [i])


n, m = map(int, input().split())
# 리스트는 1번부터 생성
n_list = list(range(1, n + 1))

solve([])
