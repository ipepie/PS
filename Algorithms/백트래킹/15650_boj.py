# 백준 15650 N과 M(2)
# 22/6/2
# 백트래킹
from itertools import combinations
from re import A
n, m = map(int,input().split())
arr = [x for x in range(1,n+1)]

li = list(combinations(arr,m))

for i in li:
    print(*i, end=' ')
    print()

'''
백트래킹 사용방식
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)

'''