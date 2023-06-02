n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
maxNum = data[n-1] #가장 큰수
secNum = data[n-2] #두 번째로 큰수
result = 0

for i in range(m) :
    if((i+1)%(k+1) != 0) :
        result = result + maxNum
    elif((i+1)%(k+1) == 0) :
        result = result + secNum
print(result)


