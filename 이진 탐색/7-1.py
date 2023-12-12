#부품 찾기

n = int(input())
exist = list(map(int, input().split()))

m = int(input())
call = list(map(int, input().split()))

def binary_search(arr, target, start, end) :
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target :
        return mid

    elif arr[mid] > target :
        return binary_search(arr, target, start, mid - 1)

    else :
        return binary_search(arr, target, mid + 1, end)
