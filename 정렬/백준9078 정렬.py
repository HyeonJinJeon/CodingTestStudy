result = []
for testCase in range(int(input())) :
    n = int(input())
    k = input().split()
    cnt = 0
    for i in range(n) :
        for j in range(i+1, n) :
            if k[i] > k[j] :
                cnt += 1

    if cnt % 2 == 0 :
        result.append('YES')
    else :
        result.append('NO')

for i in result :
    print(i)