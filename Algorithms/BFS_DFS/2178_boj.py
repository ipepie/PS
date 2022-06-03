# 백준 2178 미로탐색
# 22/6/3
# DFS/BFS
from collections import deque

def bfs(a,b):
    q = deque([(0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx>=n or ny <0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
    print(graph[n-1][m-1])

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

bfs(0,0)
