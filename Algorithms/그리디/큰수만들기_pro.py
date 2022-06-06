# 프로그래머스 큰 수 만들기
# 5/25  --> 미완성
# 그리디

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    # number의 각 숫자에 대해 위의 반복문을 모두 실행했는데도 k가 0이 되지 않는 경우
    # "654321" 처럼 내림차순으로 정렬되어있는 경우
    # k만큼 뒤에서 부터 제거
    if k !=0:
        stack = stack[:-k]
    return ''.join(stack)    
    
    # 맨마지막 이렇게해도됨
    # while k:
    #     stack.pop()
    #     k-=1

    
print(solution("1231234",3))


''' 그냥 순열 문제인줄 알고 풀었었다
from itertools import permutations
def solution(number, k):
    li = []
    for i in set((permutations(number,len(number)-k))): 
        li.append(int(''.join(i)))
    
    li.sort(reverse=True)
    
    return str(li[0])
'''