# 프로그래머스 소수 찾기
# 22/5/19
from itertools import permutations

def solution(numbers):
    answer = 0

    # 에라토스테네스의 체
    n = 10_000_000
    sieve = [True] * n
    # 인덱스와 숫자 일치시키기 위해 0,1 은 False처리
    sieve[0] = False  
    sieve[1] = False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False    
    a = len(numbers)
    
    # 순열 이용해 숫자 조합 저장 및 set으로 중복제거
    for x in range(1,a+1):
        arr = list(set(permutations(numbers,x)))
        #print(arr)
        for j in range(len(arr)):
            # '011' '11'처럼 맨 앞이 0으로 시작하는 숫자 중복 제거
            if arr[j][0] == '0':
                continue
            num = ''.join(arr[j])
            if sieve[int(num)] == True:
                #print(sieve[int(num)])
                answer += 1
    return answer

#print(solution("011"))