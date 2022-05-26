# 프로그래머스 K번째수
# 22/5/26
# 정렬

def solution(array, commands):
    answer = []
    li = []
    for x in commands:
        i, j, k = x[0],x[1],x[2]
        print(array[i-1:j])
        answer.append(sorted(array[i-1:j])[k-1])           
    
    return answer