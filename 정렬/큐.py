class MyQueue:
    def __init__(self):
        self.temp = None
        self.max_limit = 0  # 최대값 제한
        self.size = 0  # 아무것도 안설정하면 크기는 0
        self.items = []  # 내용도 비어있음
        self.able = 0  # 1 이면 limit on! 0 이면 limit off!

    def limit(self, limit):
        self.max_limit = limit  # 최대치 설정
        self.able = 1  # limit on!

    def limit_release(self):
        self.able = 0
        self.max_limit = 0

    def is_empty(self):
        if self.size == 0:  # 사이즈가 0이면 비어있는 상태 Ture
            return True
        else:
            return False  # 아니라면 False 출력

    def is_full(self):
        if self.able == 1:
            if self.size >= self.max_limit:  # size의 값이 limit 랑 같으면 꽉 참
                return True
            else:
                return False
        else:
            print("제한 설정이 없습니다.")

    def push(self, item):
        if self.able == 1:
            if self.size < self.max_limit:  # 제한 값 보다 작으면 넣음
                self.size += 1
                self.items.append(item)
            else:  # 제한 값 보다 크면 못 넣음
                print("스택이 가득 찼습니다.")
        else:
            self.size += 1
            self.items.append(item)

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

    def peekleft(self):
        if not self.is_empty():
            return self.items[0]  # 마지막 열에 있는 값 보여주기
        else:
            print("리스트가 비어 있습니다.")

    def clear(self):
        self.items = []
        self.size = 0
        self.able = 0
        self.max_limit = 0

    def is_contain(self, item):
        return item in self.items # item 이 안에 있으면 참 없으면 거짓!

    def list(self):
        return self.items


# 클래스 인스턴스 설정
queue = MyQueue()
# 비어있는지 확인
print(queue.is_empty())  # True
# 가득 찾는지 확인
print(queue.is_full())  # 제한 설정이 없습니다.
# 최대 입력수 제한 2개
queue.limit(2)
print(queue.is_full())  # False
# 1 Enqueue
queue.push(1)
print(queue.is_full())  # False
# 2 Enqueue
queue.push(2)
# 2 Enqueue
queue.push(2) # 스택이 가득 찼습니다.

print(queue.is_full())  # True
# 현재 큐 표시
print(queue.list())  # [1, 2]
# 1 처음 값 Dequeue 후 a 변수에 넣기
a = queue.popleft()
print(a)  # 1
# 2 마지막 값 Dequeue 후 a 변수에 넣기
a = queue.pop()
print(a)  # 2
# 빈 리스트
print(queue.list())  # []
# 2 Enqueue
queue.push(2)
# 리스트 초기화
queue.clear()
# 리스트 확인
print(queue.list())  # []
# 1,2,3 Enqueue
queue.push(1)
queue.push(2)
queue.push(3)
# 맨 마지막 입력 값 확인
print(queue.peek())  # 3
# 맨 처음 입력 값 확인
print(queue.peekleft())  # 1
# 큐안에 1과 0의 값이 있는지 확인
print(queue.is_contain(1))  # True
print(queue.is_contain(0))  # False
