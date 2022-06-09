# 백준 1463 1로 만들기
# 22/6/8
# DP

n = int(input())
d = [0] * (10**6+1)
d[1] = 0

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
    if i % 2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
print(d[n])