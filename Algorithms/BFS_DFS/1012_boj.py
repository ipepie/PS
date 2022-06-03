# 백준 1012 유기농 배추
# 22/6/3
# BFS/DFS

# 세로가n, 가로가 m
# n이 행 = y좌표, m이 열 = x좌표
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x-1,y)
        return True
    return False

t = int(input())
for _ in range(t):
    
    m,n,k = map(int,input().split())

    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split())
        graph[b][a] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    print(result)
