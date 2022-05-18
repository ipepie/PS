# 백준 2231 분해합
# 브루트 포스
# 22/5/18

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for x in range(1,n+1):
    a = list(map(int,str(x))) # 각 자리의 수 쪼개기
    if sum(a) + x == n:
        arr.append(x)
print(min(arr) if len(arr) != 0 else 0)

