# 프로그래머스 큰 수 만들기
# 5/25  --> 미완성
# 그리디


def solution(number, k):
    answer = ''
    li = list(number)

    for _ in range(k):
        m = li.index(min(li))
        del li[m] 

    return ''.join(li)    
    # if len(answer) == len(number) -k:


    
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