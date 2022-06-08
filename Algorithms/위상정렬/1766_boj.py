# 백준 1766 문제집
# 22/6/6
# 위상정렬

# 힙 자료구조를 이용한 우선순위 큐 이용
# 파이썬의 힙은 최소 힙. 최소값을 우선순위로 하는 우선순위 큐
# 부모노드가 자식노드보다 항상 작거나 같은 완전 이진 트리
# 형제 노드 간에는 정렬 상태 없음! 비교하지 않는다
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
