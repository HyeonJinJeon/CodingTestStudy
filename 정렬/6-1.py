n = int(input())
arr = []

for i in range(n) :
    arr.append(int(input()))

arr = sorted(arr, reverse=True)

for i in range(len(arr)) :
    print(arr[i], end=' ')