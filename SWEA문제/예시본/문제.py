import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


T = int(input())
# 여러 개의 테스트 케이스 가 주어 지므로, 각각을 처리 합니다.
for test_case in range(1, T + 1):


    print(f"#{test_case} {counter}")
