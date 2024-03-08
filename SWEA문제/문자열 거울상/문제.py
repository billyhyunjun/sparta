import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")

def mirror(text_list):
    new_list = []
    for i in text_list[::-1]:
        if i == "b":
            new_list.append("d")
        elif i == "d":
            new_list.append("b")
        elif i == "q":
            new_list.append("p")
        elif i == "p":
            new_list.append("q")
    return new_list




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    text = input()
    text_list = list(text)
    ans = "".join(mirror(text_list))
    print(f"#{test_case} {ans}")