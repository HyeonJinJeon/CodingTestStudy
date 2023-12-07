# 선택정렬 : 매번 가장 작은 것을 선택하여 맨 앞으로 차곡차곡 보내는 것

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)) :
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(arr)) :
        if arr[min_index] > arr[j] :
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] #가장 작은 값과 스와프

print(arr)