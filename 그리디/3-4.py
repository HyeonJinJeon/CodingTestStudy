n, m = map(int, input().split())

result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    minValue = 10001
    for j in data :
        minValue = min(minValue, j)
    result = max(result, minValue) #가장 작은 수에서 가장 큰 수를 찾기 ( result와 minValue를 비교하여 큰 수를 찾음 )

print(result)