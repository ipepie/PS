# 백준 15654 N과 M 5
# 22/6/10
# 백트래킹
from itertools import permutations
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

li = list(permutations(arr,m))
for i in li:
    print(*i)
