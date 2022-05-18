# 백준 2798 블랙잭
# 브루트 포스
# 22/5/18

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int,input().split()))

ans = 0
arr = []

result = list(combinations(nlist,3))
for x in result:
    if sum(x) == m:
        ans = m
        break
    elif sum(x) < m:
        arr.append(sum(x))

print(ans if ans!= 0 else max(arr))
        

