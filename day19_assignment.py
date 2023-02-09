# 11.1
def mentorsort(array):
    n = len(array)
    for end in range(1, n):
        for cur in range(end,0,-1):
            if array[cur-1][1] > array[cur][1]:
                array[cur-1],array[cur] = array[cur],array[cur-1]

    return array


student_array = [['선미',88],['초아',99],['화사',71],['영탁',78],['영웅',67],['민호',92]]

print('정렬 전 -->' ,student_array)
student_array = mentorsort(student_array)
print('정렬 후 -->' ,student_array)
print('성적별 조 편성표')
for i in range(3):
    print(f'{student_array[i][0]} : {student_array[len(student_array)-1-i][0]}')



