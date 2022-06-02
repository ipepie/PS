# 프로그래머스 네트워크
# 22/6/2
# BFS/DFS

from collections import deque
def solution(n, computers):
    answer = 0

    visited = [False] * (n+1)
    visited[0] = True
    # computers 배열내의 1을 연결된 컴퓨터의 번호로 변경
    computers = [[]] + computers
    for i in computers:
        for a,b in enumerate(i):
            if b == 1:
                i[a] = a+1
    for x in range(1,n+1):
        # 시작노드와 연결이 안된 (방문안한) 노드의 경우 해당 노드에서 다시 bfs
        if not visited[x]:
            bfs(x,computers,visited)
            answer +=1
    return answer

def bfs(start,computers,visited):
    q = deque([start])
    visited[0] = True
    while q:
        a = q.popleft()
        visited[a] = True
        for i in computers[a]:
            if not visited[i]:
                q.append(i)

# solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])

