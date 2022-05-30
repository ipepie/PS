# 백준 N과 M(1)
# 22/5/30
# 백트래킹
from itertools import permutations
n,m = map(int,input().split())

li = [x for x in range(1,n+1)]
a = list(permutations(li,m))

for x in a:
    for y in x:
        print(y, end= ' ')
    print()
