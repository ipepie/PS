# 백준 24479 깊이 우선 탐색 1
# 22/5/27
# DFS

# n, m 오타 때문에 하루종일 런타임 에러나서 디버깅만 두시간 걸린 문제
# 접근은 다른 해설봐도 똑같다 전형적인 DFS
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, r = map(int,input().split())
graph = [[] for x in range(n+1)]

for _ in range(m):
    i, v = map(int,input().split())
    graph[i].append(v)
    graph[v].append(i)

for i in range(n+1):
    graph[i].sort()

cnt = 0
visited = [False] * (n+1)
answer = [0] * (n+1)

def dfs(graph,r,visited):
    visited[r] = True
    global cnt
    cnt += 1
    answer[r] = cnt
    
    for i in graph[r]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,r,visited)
for x in answer[1:]:
    print(x)