n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

arr.sort()

for i in range(arr[n-1], 0, -1) :
    for j in range(n) :
        if arr[j] > i :
            result = result + (arr[j] - i)
        else :
            continue
    if result < k :
        result = 0
        continue
    elif result >= k :
        print(i)
        break