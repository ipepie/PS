# 백준 1463 1로 만들기(2)
# 22/6/8
# DP, 그래프 탐색

n = int(input())
d = [0] * (10**6+1)
d[1] = 0
ans = [0] * (n+1) 

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    ans[i] = i-1
    if i % 3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
        ans[i] = i//3
    if i % 2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
        ans[i] = i//2
print(d[n])
print(ans)

m = n
while ans[m] != 0:
    print(ans[m],end=' ')
    m = ans[m]