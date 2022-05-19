# 프로그래머스 124나라
# 22/5/19
def solution(n):
    
    arr = []
    while n > 0:
        m = n%3
        if m == 0:
            arr.append('4')
            n = (n-1)//3
        else:
            arr.append(str(n%3))
            n = n//3 
    return(''.join(arr[::-1]))

# 테스트
print(solution(19))