# 프로그래머스 단어 변환
# 22/6/5
# DFS/BFS

from collections import deque
def solution(begin, target, words):
    # words안에 target이 없으면 변환 불가
    if target not in words:
        return 0

    # 한번 변환한 후 다시 예전으로 변환하지 않기위해 방문 여부 체크
    visited = [False] * len(words)
    q = deque()
    q.append((begin,0))
    while q:
        cur, idx = q.popleft()
        n = 0
        # bfs 순회중 가장 먼저 target과 일치했을 때의 변환 횟수 리턴
        if cur == target:
            return idx

        for i in range(len(words)):
            if not visited[i]:
                # 하나의 알파벳만 바꿀 수 있으므로 바꿀 수 있는 모든 단어를 큐에 추가
                for j in range(len(target)):
                    if cur[j] != words[i][j]:
                        n += 1
                    if n>1:
                        n=0
                        break
            if n == 1:
                q.append((words[i],idx+1))
                visited[i] = True
                n=0
        
# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))