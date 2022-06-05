# 백준 15649 N과 M(1)
# 22/5/30
# 백트래킹

# 순열로 풀긴했는데 정해가 아닌 것 같다
from itertools import permutations
n,m = map(int,input().split())

li = [x for x in range(1,n+1)]
a = list(permutations(li,m))

for x in a:
    for y in x:
        print(y, end= ' ')
    print()

# 백트래킹 풀이
'''
n,m = map(int,input().split())
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
'''