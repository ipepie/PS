# 백준 7576 토마토
# 22/6/10
# BFS/DFS

from collections import deque
m,n = map(int,input().split())

q = deque()
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs():
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx>= n or ny <0 or ny>=m or graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs()
day = 0
for i in graph:
    day = max(day,max(i)-1)    
    if 0 in i:
        print(-1)
        exit(0)
print(day)