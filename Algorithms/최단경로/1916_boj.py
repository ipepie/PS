# 백준 1916 최소비용 구하기
# 22/6/9
# 다익스트라

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())

distance = [INF] * (n+1) 
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0
    while pq:
        dis, cur = heapq.heappop(pq)
        if dis > distance[cur]:
            continue
        for i in graph[cur]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq,(cost,i[0]))

s,e = map(int,input().split())
dijkstra(s)
print(distance[e])