# 백준 24444 너비 우선 탐색 1 
# 22/6/5
# BFS
import sys
from collections import deque
input = sys.stdin.readline
n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a) 

for i in graph:
    i.sort()

ans = [0] * (n+1)
def bfs(r):
    q = deque()
    q.append(r)
    visited[r] = True
    cnt = 1
    ans[r] = cnt
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
                ans[i] = cnt
                
bfs(r)
# ans에는 순회 순서대로 들어감
print(*ans[1:],sep='\n')