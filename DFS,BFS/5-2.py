from collections import deque


n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()

        # 상하좌우를 확인하여 움직일 수 있는 곳인지 판별
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 영역 밖으로 이동하려고 할 때
            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue

            # 벽으로 막혀있는 곳으로 이동하려고 할 때
            if graph[nx][ny] == 0 :
                continue

            # 이동할 수 있는 곳으로 이동 할 때
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1 # 1인 곳을 이동하고 최단거리를 구하기 위해 전 영역의 수에 1을 더한다
                queue.append((nx, ny)) # 이동한 곳을 큐에 넣어준다
    return graph[n-1][m-1] #마지막 영역을 리턴

print(bfs(0, 0))