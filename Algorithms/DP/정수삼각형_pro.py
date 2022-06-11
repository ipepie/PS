# 프로그래머스 정수삼각형
# 22/6/10
# DP, BFS사용함

# 이차원 리스트는 그냥 copy()랑 1차원 슬라이싱, extend로 깊은복사가 안됨

from copy import deepcopy
def solution(triangle):
    d = deepcopy(triangle)
    # d = [i[:] for i in triangle]이 더 효율적
    def bfs(depth,idx):
        for _ in range(depth+1):
            d[depth+1][idx] = max(d[depth+1][idx],d[depth][idx] + triangle[depth+1][idx])
            d[depth+1][idx+1] = max(d[depth+1][idx+1],d[depth][idx] + triangle[depth+1][idx+1])
            idx += 1    

    for i in range(len(triangle)-1):
        bfs(i,0)

    return max(d[-1])