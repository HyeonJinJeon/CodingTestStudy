#개미 전사
# d[1]
# d[2]
# d[3] = d[1] + d[3]
# d[4] = d[2] + d[4]
# d[5] = d[1] + d[3] + d[5]
# d[6] = d[2] + d[4] + d[6]
# d[7] = d[1] + d[3] + d[5] +d[7]

# 짝수는 짝수만 홀수는 홀수만 더하는 수열

n = int(input())

arr = list(map(int,input().split()))

d = [0] * 1001

for i in range(3, n+1) :
    d[i] = max(arr[i-2], arr[i-3] + arr[i-1])

print(d[i])