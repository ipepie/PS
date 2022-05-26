# 프로그래머스 가장 큰 수
# 22.5.26
# 정렬

# 순열써서 풀었었는데 시간초과
def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers의 원소가 0이상 1000이하 이므로 각원소를 최소 세자리수로 맞춰서 정렬
    numbers.sort(reverse = True, key = lambda x : x*3)
    # '000' 등의 경우 숫자 형태로 변환
    return str(int(''.join(numbers)))
    
#print(solution([6,10,2]))