# 백준 24416 알고리즘 수업 - 피보나치 수 1
# 22/6/8
# DP

n = int(input())

d = [0] *(n+1)
d[1]=1
d[2] = 1
a = 0
for i in range(3,n+1):
    a += 1
    d[i] = d[i-1] + d[i-2]

print(d[n],a)