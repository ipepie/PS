# 프로그래머스 이중우선순위큐
# 22/6/9
# 힙

import heapq
def solution(operations):
    answer = [0,0]
    
    h = [] # 최소힙
    mh = [] # 최대힙
    for i in operations:
        o, n = i.split()
        if o == 'I':
            heapq.heappush(h,int(n))
            heapq.heappush(mh,-int(n))
        else:
            # 힙에 원소가 없는데 D인 경우 패스
            if len(h) == 0:
                continue
            
            # 최대값 제거
            if int(n) == 1:
                heapq.heappop(mh)
                # 두 힙의 현재 크기가 1일 수 있으니 최소힙에서도 하나 삭제
                h.pop()
            # 최소값 제거
            elif int(n) == -1:
                heapq.heappop(h)
                # 마찬가지로 최대힙에서도 삭제
                mh.pop()
    if len(h) == 0:
        return answer
    return [-mh[0],h[0]]
    