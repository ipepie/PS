# 백준 1753 최단경로
# 22/6//9
# 다익스트라

import sys
import heapq
input = sys.stdin.readline
# 무한 값 설정
INF = 1e9 # 10억
v, e = map(int,input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# 최단거리 테이블을 무한으로 초기화
distance = [INF] * (v+1)
def dijkstra(start):
    pq = []
    # 시작 노드로 가는 최단거리는 0으로 하여 큐에 삽입
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        dis, cur = heapq.heappop(pq)

        # 현재 노드가 이미 처리된 적이 있으면 패스
        if distance[cur] < dis:
            continue

        for i in graph[cur]:
            cost = dis + i[1]
            # 현재 노드를 거쳐서 대상 노드로(i[0]) 이동하는 거리가 더 짧을 경우 최단거리 테이블의 노드 인덱스 값을 변경
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq,(cost,i[0]))

dijkstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])