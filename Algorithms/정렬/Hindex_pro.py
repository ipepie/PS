# 프로그래머스 H-index
# 22/5/25
# 정렬

# H-index : 인덱스가 해당 배열의 인덱스 값보다 크거나 같은 경우의 최대값
# 위키에서 개념 이해..

def solution(citations):
    citations.sort(reverse=True)

    for i, v in enumerate(citations):
        if i >= v:   
            return(i)
    # 인용횟수가 인덱스보다 큰 수들밖에 없으면 해당 배열의 크기 리턴
    # [100,200]
    return(len(citations))

# print(solution([3, 0, 6, 1, 5]))