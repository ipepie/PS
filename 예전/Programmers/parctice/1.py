# 로또의 최고 순위와 최저 순위 - level1
# 22/1/4

def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    match = 0
    a = lottos.count(0)
    #max, min = 0,0
    for x in lottos:
        if x in win_nums:
            match += 1
    max = match + a
    min = match 
    return(rank[max],rank[min])
    