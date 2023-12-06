n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveType = ['L', 'R', 'U', 'D']

for plan in plans :
    for i in range(len(moveType)) : #len(moveType)은 4를 생성하고 range는 0,1,2,3을 생성한다
        if plan == moveType[i] : #moveType[0] = L, moveType[1] = R, mvoeType[2] = U, moveType[3] = D
            nx = x + dx[i]
            ny = y + dy[i]
    if (nx < 1) | (ny < 1) | (nx > n) | (ny > n) :
        continue
    x, y = nx, ny

print(x, y)