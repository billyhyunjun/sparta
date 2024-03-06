# 나무 갯수 원하는 나무길이
n, m = map(int, input().split())
# 나무 높이
trees = list(map(int, input().split()))
# 가장 높은 나무
heighten_tree = max(trees)
cut_height = 0


# 재귀 입장
def cut_tree(low, high):

    # 전역 변수 가져오기
    global m
    global cut_height

    # 기저 사례~
    if low > high:
        return

    # 나무 중앙 값
    mid = (low + high) // 2
    taken_tree = 0

    # 나무들 자르자
    for tree in trees:
        if tree > mid:
            taken_tree += tree - mid
    # 자른 나무 양이 목표치 보다 클때
    if taken_tree >= m:
        cut_height = mid
        cut_tree(mid + 1, high)
    # 자른 나무 양이 모자랄 때
    else:
        cut_tree(low, mid - 1)


cut_tree(0, heighten_tree)
print(cut_height)
