# 프로그래머스 전력망을 둘로 나누기
# 22/6/9
# 백트래킹

from collections import deque
from itertools import combinations
def solution(n, wires):
    ans = []
    
    def bfs(start,graph,visited):       
        q = deque([start])
        visited[start] = True
        cnt = 0
        answer = 100
        while q:
            cnt += 1
            cur = q.popleft()
            for i in graph[cur]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        gap = abs(cnt - (n-cnt))
        # answer의 최대값 100 보다 작은 경우 해당 값으로 교체해서 return할 ans리스트에 추가
        if answer > gap:
            answer = gap
            ans.append(answer)

    # wires에서 하나의 간선을 제외한 경우를 모두 골라 반복문 돌면서 해당 그래프를 bfs
    xwires = list(combinations(wires,n-2))
    for wires in xwires:
        graph = [[] for _ in range(n+1)]
        for i in wires:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        if [] not in graph[1:]:
            visited = [False] * (n+1)
            bfs(i[0],graph,visited)
    
    # 어느 간선이든 하나를 자르게되면 바로 두개의 그룹으로 나누어 지는 경우.
    # 테스트 케이스 1번
    if ans == []:
        return n-2
    return min(ans)

# print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

''' 
다른풀이 bfs 이렇게 접근하면 그래프 간선 하나씩 자른거 그때그때 생성안해도 되겠다.
    def bfs(start, skip):  
        visited = [False] * (n+1)
        q = deque([start])
        visited[start] = True
        cnt = 0
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if not visited[i] and i != skip:
                    visited[i] = True
                    q.append(i)
            cnt += 1
        print(cnt)
        cnt2 = n - cnt
        gap = abs(cnt - cnt2)
    
        if gap < answer:
            answer = gap
그래프는 처음입력대로 받고,
for문을 wires의 크기만큼 돌려서
start, skip = wires[i]
로 bfs하고 answer의 최소값 리턴받기
'''