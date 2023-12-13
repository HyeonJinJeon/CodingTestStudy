#부품 찾기

n = int(input())
exist = list(map(int, input().split()))

m = int(input())
call = list(map(int, input().split()))

exist.sort()
call.sort()

def binary_search(exist, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if exist[mid] == target :
            return print("yes", end=" ")
        elif exist[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return print("no", end=" ")

for j in range(m) :
    binary_search(exist, call[j], 0, n-1)