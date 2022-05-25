# 프로그래머스 큰 수 만들기
# 5/25
# 그리디

from itertools import permutations
def solution(number, k):
    answer = ''
    li = list((permutations(number,k)))
    print(li)

    return answer

solution("1924",2)