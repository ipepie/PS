# 백준 1759 암호 만들기
# 22/6/9
# 브루트포스, 백트래킹

from itertools import combinations
l, c = map(int,input().split())
arr = input().split()
arr.sort()
li = [i for i in combinations(arr,l)]
# print(li)

def check(list,n):
    cnt = 0
    for x in list:
        if x in 'aeiou':
            cnt += 1
    if 1 <= cnt <=n-2:
        return True

for i in li:
    if check(i,l):
        print(''.join(i))


