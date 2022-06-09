# 백준 1987 알파벳
# 22/6/9
# 백트래킹

r, c = map(int,input().split())

graph = []
for _ in range(r):
    row = []
    for i in list(input()):
        row.append(ord(i)-ord('A')+1)
    graph.append(row)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = 1
visited = [False] * 27
def dfs(cnt,x,y):
    global ans
    if ans < cnt:
        ans = cnt
    cur = graph[x][y]
    visited[cur] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or nx>=r or ny <0 or ny>=c:
            continue
        if not visited[graph[nx][ny]]:
            visited[graph[nx][ny]] = True
            dfs(cnt+1,nx,ny)
            visited[graph[nx][ny]] = False
dfs(1,0,0)
print(ans)