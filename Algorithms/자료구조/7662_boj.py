# 백준 7662 이중 우선순위 큐
# 22/6/9 
# 우선순위큐
import sys
import heapq
input = sys.stdin.readline

t = int(input())


# 테스트 케이스만큼 반복한다.
for _ in range(t):
    q = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * q # 삽입 후 삭제 여부 확인 용도

    
    for i in range(q):
        o, n = input().split()

        if o == "I":
            heapq.heappush(max_heap, (-int(n), i)) # 최대 힙
            heapq.heappush(min_heap, (int(n), i)) # 최소 힙
            visited[i] = True # 정수 생성

        else:
            if n == "1":
                # 반복문을 통해 이미 제거 된 정수는 팝하여 제거
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)

                # 최대 힙이 있으면 최대 힙 제거
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            else:
                # 반복문을 통해 이미 제거된 정수는 팝하여 제거
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)

                # 최소 힙이 있으면 최소 힙 제거
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print('EMPTY')        
