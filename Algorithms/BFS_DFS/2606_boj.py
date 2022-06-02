# 백준 2606 바이러스
# 22/6/2
# BFS, DFS

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
def dfs(r):
    visited[r] = True
    global count

    for i in graph[r]:
        if not visited[i]:
            count += 1
            dfs(i) 
dfs(1)
print(count)
