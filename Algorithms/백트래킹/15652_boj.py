# 백준 15649 N과 M(4)
# 22/6/2
# 백트래킹

from itertools import combinations_with_replacement
n,m = map(int,input().split())

li = [x for x in range(1,n+1)]
a = list(combinations_with_replacement(li,m))

for x in a:
    print(*x,end=' ')
    print()