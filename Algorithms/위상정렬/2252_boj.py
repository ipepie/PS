# 백준 2252 줄 세우기
# 22/6/6
# 위상정렬
from collections import deque
n,m = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    # 위상정렬은 DAG 방향 그래프. a에서 b로 이동(줄 세우기)
    graph[a].append(b)
    # 진입차수를 1씩 증가
    indegree[b] += 1

ans = []
q = deque()
# 먼저 진입차수가 0인 노드를 큐에 삽입
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    ans.append(cur)
    for x in graph[cur]:
        indegree[x] -= 1
        # 새로 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[x] == 0:
            q.append(x)

print(*ans)