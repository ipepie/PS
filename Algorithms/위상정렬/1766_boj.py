# 백준 1766 문제집
# 22/6/6
# 위상정렬

import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
heap = []
ans = []
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
while heap:
    cur = heapq.heappop(heap)
    ans.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap,i)
print(*ans)
