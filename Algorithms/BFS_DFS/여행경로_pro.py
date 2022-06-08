# 프로그래머스 여행경로
# 22/6/7
# DFS/BFS

# 유사 딕셔너리 자료구조 처음 사용
# 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해줌.
from collections import defaultdict
def solution(tickets):
    answer = []
    tickets.sort()
    route = defaultdict(list)
    
    for key, value in tickets:
        route[key].append(value)
    # 리스트를 생성자로 defaultdict를 생성해서 value 값이 없으면 빈 리스트로 저장되게끔 함
    # {'ATL': ['ICN', 'SFO'], 'ICN': ['ATL', 'SFO'], 'SFO': ['ATL']})
    def dfs():
        # 출발지
        stack = ['ICN']

        while stack:
            # 현재 출발지에서 출발하는 티켓이 없으면 최종 목적지가 됨. 마지막에 목적지를 역순으로 출력
            # 스택에 여전히 남아있게 된다.
            top = stack[-1]
            if top not in route or route[top] == []:
                answer.append(stack.pop())
            # 출발 티켓이 있는 경우
            else:
                # 위의 조건문에서 route != [], 즉 다른 목적지로 향하는 티켓이 존재
                # 알파벳 오름차순으로 정렬된 상태이므로 다음 출발 장소에 추가
                stack.append(route[top].pop(0))
    dfs()
    return answer[::-1]

# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])