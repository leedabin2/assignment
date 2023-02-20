# 13-1  정렬과 이진검색

import random

def search(array, find_data):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_data == array[mid]:
            return mid
        elif find_data > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


data_array = ['코카콜라','츄파츕스','도시락','삼각김밥','바나나우유','레쓰비캔커피']
sell_array = [random.choice(data_array) for _ in range(20)]


print('오늘 판매된 전체 물건(중복O, 정렬X) -->', sell_array)
sell_array.sort()
print('오늘 판매된 전체 물건(중복O, 정렬O) -->', sell_array)
sell_product = list(set(sell_array))  # set - list에서 중복제거 가능
print('오늘 판매된 물품 종류(중복x) -->', sell_product)

count_list = []
for product in sell_product:
    count = 0
    position = 0
    while position != -1:
        position = search(sell_array, product)
        if position != -1:
            count += 1
            del(sell_array[position])
    count_list.append((product, count))

print()
print("결산 결과 ==>", count_list)
print()

# 13-2

def seq_search(array, find_data) :
    global count
    position = -1
    for i in range(len(array)):
        count += 1
        if array[i] == find_data:
            position = i
            break
    return position

def bin_search(array, find_data):
    global count
    start = 0
    end = len(array) - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2

        if find_data == array[mid]:
            return mid
        elif find_data > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


data_arr, sorted_arr = [], []
finddata = 7878
count = 0


data_arr = [random.randint(0, 1000000) for _ in range(1000000)]
data_arr.insert(random.randint(0, 1000000), finddata)
sorted_arr = sorted(data_arr)

print(f'비정렬 배열(100만개) --> {data_arr[0:5]} ~~~~ {data_arr[-5:len(data_arr)]}')
print(f'정렬 배열(100만개) --> {sorted_arr[0:5]} ~~~~ {sorted_arr[-5:len(sorted_arr)]}')

count = 0
pos = seq_search(data_arr, finddata)
if pos != -1:
    print(f'순차 검색(비정렬 데이터) --> {count}회')

count = 0
pos = bin_search(sorted_arr, finddata)
if pos != -1:
    print(f'이진 검색(정렬 데이터) --> {count}회')




