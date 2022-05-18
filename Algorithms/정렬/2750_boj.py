# 백준 2750 수 정렬하기
# 정렬
# 22/5/19

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

for i in range(n):
    print(arr[i])
