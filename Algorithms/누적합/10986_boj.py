# 백준 10986 나머지 합
# 22/6/7
# 누적 합

# 조합 추가
# 나머지가 동일한 구간합을 찾아서 nC2
# O(n+m) 시간복잡도로 풀어야 함
# (구간 (1,4) 의 합 의 나머지..)  ==   (구간 (1,1) 의나머지 )  
#  - > (2,4) 구간합의 나머지
# 모듈러 연산에 의해  
# (PrefixSum[j] - PrefixSum[i] ) % MOD = 0 이 만족한다면
# PrefixSum[j] % MOD = PrefixSum[i] % MOD 도 만족하게 된다.
# 어렵다 이걸 어떻게 생각하나
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
ps = [0]
ps_m = [0] * m
sum = 0
for i in arr:
    sum += i
    ps.append(sum)
    ps_m[sum%m] += 1

# 나머지가 0인 경우에는 구간합끼리 비교할 필요 없이 단독으로 m으로 나누어 떨어지기 때문에 
# 나머지가 0인 경우도 각각 ans에 더해줘야 함
ans = ps_m[0]

for i in range(m):
    ans += (ps_m[i] * (ps_m[i]-1)) // 2;

# 이렇게 풀면 n**2으로 시간초과
# for start in range(1,len(arr)):
#     end = start
#     while end <= len(arr):
#         if (ps[end] - ps[start-1]) % m == 0: 
#             ans += 1
#         end += 1

print(ans)