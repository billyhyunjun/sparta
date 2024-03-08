# 버블정렬을 만들어 보자!
def bubble_sort(array):
    # 비교를 해야 하는데 처음에는 8자리까지 그다음은 7자리......마지막은 0자리로 끝이 나게
    for i in range(len(array) - 1,0,-1):
        # 8,7,6,5,4,3,2,1순으로 들어간다.
        for j in range(i):
            if array[j] > array[j+1]:
                # 서로 위치 바꾸기
                array[j],array[j+1] = array[j+1],array[j]
    return array




# 엉망 진창 리스트!
list = [1,5,4,8,6,2,7,3,9]
# 함수 호출!
sorted_list = bubble_sort(list)

print(sorted_list)