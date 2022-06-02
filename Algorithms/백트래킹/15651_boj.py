# 백준 15649 N과 M(3)
# 22/6/2
# 백트래킹

from itertools import product
n,m = map(int,input().split())

li = [x for x in range(1,n+1)]
a = list(product(li,repeat=m))

for x in a:
    print(*x,end=' ')
    print()