# 효율적인 화폐 구성
# N가지 종류의 화폐
# 화폐의 개수를 최소한으로 히용하여 합이 M원

n ,m = map(int, input().split())

arr = []

for i in range(n) :
    arr.append(int(input()))

d = [10001] * (m+1) # DP테이블을 10001로 초기화

d[0] = 0

for i in range(n) : #만약 화폐 종류가 2, 3, 5라면 2인 경우를 먼저 확인하고 d[2], d[4], d[6]...에 먼저 값을 넣어주고 3인경우, 5인경우를 따진다.
    for j in range(arr[i], m+1) :
        if d[j-arr[i]] != 10001 : # (현재 위치(가격) - 화폐의 단위)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-arr] + 1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])