class MyStack:
    def __init__(self):
        self.max_limit = -1
        self.size = 0  # 아무것도 안설정하면 크기는 0
        self.items = []  # 내용도 비어있음
        self.able = -1  # -1이 되면 꽉찬거임

    def limit(self, limit):
        self.max_limit = limit  # 최대치 설정

    def is_empty(self):
        if self.size == 0:  # 사이즈가 0이면 비어있는 상태 Ture
            return True
        else:
            return False  # 아니라면 False 출력

    def is_full(self):
        if self.max_limit == -1:
            print("제한 설정이 없습니다.")
        if self.size >= self.max_limit:  # size의 값이 limit 랑 같으면 꽉 참
            return True
        else:
            return False

    def push(self, item):
        if self.max_limit == -1:
            self.size += 1
            self.items.append(item)
        if self.size < self.max_limit:  # 제한 값 보다 작으면 넣음
            self.size += 1
            self.items.append(item)
        else:  # 제한 값 보다 크면 못 넣음
            print("스택이 가득 찼습니다.")

    def pop(self):
        if not self.is_empty():
            self.temp = self.items[-1]  # 마지막 열에 있는 값 따로 저장
            del self.items[-1]  # 마지막 열 제거
            self.size -= 1
            return self.temp  # 따로 넣어 둔 값 리턴
        else:
            print("리스트가 비어 있습니다.")

    def popleft(self):
        if not self.is_empty():
            self.temp = self.items[0]  # 가장 왼쪽 열에 있는 값 따로 저장
            del self.items[0]  # 가장 왼쪽 열 제거
            self.size -= 1
            return self.temp  # 따로 넣어 둔 값 리턴
        else:
            print("리스트가 비어 있습니다.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # 마지막 열에 있는 값 보여주기
        else:
            print("리스트가 비어 있습니다.")

    def clear(self):
        self.items = []
        self.size = 0

    def is_contain(self, item):
        return item in self.items # item 이 안에 있으면 참 없으면 거짓!

    def list(self):
        return self.items


stack = MyStack()
print(stack.is_empty())
stack.limit(2)
print(stack.is_full())
stack.push(1)
print(stack.is_full())
stack.push(2)
print(stack.is_full())
stack.push(2)
print(stack.is_full())
print(stack.list())
a = stack.pop()
print(a)
print(stack.list())
a = stack.popleft()
print(a)
stack.push(2)
stack.clear()
print(stack.list())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.push(1)
print(stack.is_contain(1))
print(stack.is_contain(0))
