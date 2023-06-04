n = int(input())
cnt = 0

for i in range(n+1) : # 시는 0시부터 시작하므로 n+1을 헤야된다
    for j in range(60) : # 60분과 60초눈 다음 단위로 넘어가기 때문에 +1이 필요 없음
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                cnt = cnt + 1

print(cnt)