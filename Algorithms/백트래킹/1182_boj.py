# 백준 1182 부분수열의 합
# 22/6/8
# 브루트포스, 백트래킹

# 그냥 조합으로 품
import sys
from itertools import combinations
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0

for i in range(1,n+1):
    li = list(combinations(arr,i))
    for x in li:
        if sum(x) == s:
            cnt += 1
print(cnt)

'''
백트래킹 풀이
 def dfs(idx, sum):
    global cnt

    if idx >= n:
        return

    # 만약 더한 수와 만들 수가 같다면 cnt + 1
    sum += arr[idx]
    if sum == s:
        cnt += 1

    # 해당 index의 수열을 더한 부분 수열과 그렇지 않은 부분 수열로 나눈다.
    dfs(idx + 1, sum)
    dfs(idx + 1, sum - arr[idx])

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
[출처] [Python] 백준 1182번 : 부분수열의 합|작성자 재창
'''


# 처음엔 투포인터 문제인줄 부분연속수열이 아니었다.
# cnt = 0
# ans = 0
# end = 0

# for start in range(n):
#     while ans < s and end < n:
#         ans += arr[end]
#         end += 1
#     if ans == s:
#         cnt += 1
#     ans -= arr[start]
# print(cnt)