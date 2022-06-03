# 백준 2667 단지번호붙이기
# 22/6/3
# BFS/DFS
from collections import deque
def bfs(a,b):
    if graph[a][b] == 0:
        return
    q = deque([(a,b)])
    cnt = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    graph[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    ans.append(cnt)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
ans = []

for i in range(n):
    for j in range(n):
        bfs(i,j)
ans.sort()
print(len(ans))
print(*ans,sep = '\n') 
# Unpacking Operator와 구분자 이용해서 한줄씩 출력