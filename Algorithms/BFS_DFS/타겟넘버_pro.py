# 프로그래머스 타겟넘버
# 22/5/23
# DFS/BFS

# BFS 풀이
from collections import deque
def solution(numbers, target):
    answer = 0
    # 현재 합과, numbers의 몇 번째 인덱스까지 진행했는지 저장하기 위한 큐 생성
    queue = deque([(0,0)])
        
    while queue:
        cur, cur_idx = queue.popleft()

        # 모든 탐색이 완료되었을 때 합
        if cur_idx == len(numbers):
            if cur == target:
                answer += 1
        # 나머지 탐색 진행
        else:
            number = numbers[cur_idx]
            queue.append((cur+number, cur_idx+1))
            queue.append((cur-number, cur_idx+1))

    return answer