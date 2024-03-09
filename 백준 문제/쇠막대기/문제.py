import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 레이저와 파이프 위치 입력
laser = input()
# 잘린 파이프 확인!
stack = []
# 파이프 갯수 저장
pipe = 0
# 레이저 ) 인지 파이프 )인지 판단
flag = True
# 글자 하나씩 전진!
for char in laser:
    # 여는 괄호면 파이프거나 레이저 일 수 있지만 일단 스택 넣기
    if char == "(":
        stack.append(char)
        flag = True
    # 맨 처음으로 닫는 괄호가 나오면 그건 레이저 다 파이프를 자르자
    elif char == ")":
        # 맨 처음 만나는 괄호 인지 아닌지
        if flag:
            # 레이저로 넣었던 (는 필요 없으니 빼 내기
            stack.pop()
            # 스택에 들어있는 파이프 만큼 파이프에 저장
            pipe += len(stack)
            # 이제 뒤에 연달아 나오는 )는 레이저가 아니라 파이프 입니다.
            flag = False
        # 연달아오는 )
        else:
            # 파이프 하나 빼고
            stack.pop()
            # 꼬다리 파이프 챙겨
            pipe += 1

print(pipe)
