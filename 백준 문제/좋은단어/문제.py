import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


# 테스트 반복 !
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 입력받을 줄의 갯수 구하기
    num = int(input())
    # 합격한 문장의 수
    cnt = 0

    # 반복문 들어 가면서 검사 받을 문장 입력
    for _ in range(num):
        text_line = input().rstrip()
        stack = []

        # stack에서 append와 pop을 이용해서 짝 맞추기!
        for i in range(len(text_line)):
            # stack내부에 값이 존재하고 맨 마지막으로 넣었던 값이 지금 비교하고 싶은 값과 같다면 가지고 나가기
            if stack and text_line[i] == stack[-1]:
                stack.pop()
            # 안에 값이 없거나 지금 내가 들고 있는 문자랑 값이 다르다면 맨위로 값을 넣기
            else:
                stack.append(text_line[i])
        # 모든 짝이 맞추어 stack의 값이 아무것도 없다면 재대로된 문자열로 포인트 1점
        if not stack:
            cnt += 1

    print(cnt)