# 프로그래머스 다리를 지나는 트럭
# 22/5/22
# 스택/큐

from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0 # 시간
    w = 0 # 다리의 현재 무게
    bridge = deque([0] * bridge_length)
    # 트럭리스트에 데이터가 없을 때까지 반복
    while truck_weights:
        #print(truck_weights)
        cnt += 1
        w -= bridge.popleft()
        # 다리 무게보다 작으면 다리에 트럭 추가하고 맨처음 요소 제거
        if truck_weights[0] + w <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            w += truck
        else:
            bridge.append(0)
    # 다리에 마지막 차가 올라가고 난 후 다리 길이만큼의 시간 소요
    answer = cnt + bridge_length
    return answer

#print(solution(2,10,[7,4,5,6]))