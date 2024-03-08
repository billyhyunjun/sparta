import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def patton(text, length):
    for i in range(length):
        for j in range(1,length+1):
            if text[i:j] == text[i+j:j*2]:
                return text[i:j]



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = input()
    num_length = len(num)
    text = len(patton(num, num_length))

    print(f"#{test_case} {text}")
