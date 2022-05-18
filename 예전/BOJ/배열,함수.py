#10818
import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().split()))
print(min(num),max(num))

#2562
import sys
input = sys.stdin.readline
n = []
for _ in range(9):
    n.append(int(input()))
print(max(n))
print(n.index(max(n))+1)


#2577
import sys
input = sys.stdin.readline
a= int(input())
b= int(input())
c= int(input())
d = str(a*b*c)
for i in range(10):
    print(d.count(str(i)))

#3052
import sys
input = sys.stdin.readline
ans = set()
for i in range(10):
    n = int(input())
    ans.add(n%42)
print(len(ans))

#1546
import sys
input = sys.stdin.readline
N = int(input())
score = list(map(int,input().split()))
M = max(score)
new = []
for i in score:
    new.append(i/M*100)
print(sum(new)/N)

#8958
import sys
input = sys.stdin.readline
N = int(input())
for x in range(N):
    score = 0
    ans = input().replace('X',' ').split()
    for y in ans:
        score += sum(range(1,len(y)+1))
    print(score)
#sum(range())도 되네 마지막 for문 안써도될듯
#for z in range(1,len(y)+1):
#            score += z
#원래 이렇게 풀었었음. 근데 이게 시간이 더 적게드네

#4344
import sys
input = sys.stdin.readline
C = int(input())
for i in range(C):
    N = list(map(int,input().split()))
    del N[0]
    M = sum(N)/len(N)
    H = 0
    for x in N:
        if x > M:
            H += 1
    print('{:.3%}'.format(H/len(N)))

#15596
def solve(x):
    return sum(x)

#4673 첫실버5 문제이해!
natrual_number = set(range(1,10001))
generated_number = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_number.add(i)
self_number = natrual_number - generated_number
for i in sorted(self_number):
    print(i)

#1065
N = int(input())
ans = 0
for i in range(1,N+1):
    if i<100:
        ans += 1
    elif 100<= i <1000:
        if int(str(i)[1])*2 == i//100 + i%10:
            ans += 1
    else:
        ans = 144
print(ans)
#문제 푸는 방향은 제대로 맞은듯. 근데좀 N이 1000일 때 값을 144로 떄려박는게 거슬렸는데
#어차피 1000은 한수가 아닌거 알고 있었으니까 else로 한번에 그냥 세번째-두번쨰 = 두번째-첫번째로
#조건문 세워서 ans +=1했어도 됐을듯.
