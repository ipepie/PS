# 프로그래머스 프린터
# 22/5/24
# 스택/큐

from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    # 인덱스와 우선순위 함께 큐에 추가
    for i, v in enumerate(priorities):
        queue.append((i,v))

    while queue:
        # 큐의 처음 요소의 중요도가 가장 크면 출력
        if queue[0][1] == max(priorities):
            
            answer += 1
            # 우선순위 리스트에서 삭제
            priorities.remove(queue[0][1])
            # 원하는 인덱스의 문서인지 확인
            if queue[0][0] == location:
                return answer
            # 출력했으니 큐에서 제거
            queue.popleft()
        
        else:
            queue.append(queue.popleft())

    
    


# print(solution([1, 1, 9, 1, 1, 1],0))