# 프로그래머스 모의고사
# 22/5/19
# 완전탐색

def solution(answers):
    m1 = [1, 2, 3, 4, 5] # 5개
    m2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8 
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    a = b = c = 0
    for i in range(len(answers)):
        if answers[i] == m1[i%5]:
            a += 1
        if answers[i] == m2[i%8]:
            b += 1
        if answers[i] == m3[i%10]:
            c += 1
    answer = []
    largest = max(a,b,c)
    if largest == a:
        answer.append(1)
    if largest == b:
        answer.append(2)
    if largest == c:        
        answer.append(3)
    return answer
# print(solution([1,2,3,4,5]))