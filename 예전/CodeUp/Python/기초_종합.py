#Code Up - Python 기초100제 
#2022/1/25 
#파이썬 오랜만이라 기초 복습 용도.

# 6077 - 짝수 합 구하기
n = int(input())
sum = 0
for x in range(1,n+1):
    if x%2 == 0:
        sum+=x
print(sum)

# 6078 - 원하는 문자가 입력될 때까지 반복출력하기
while True:
    a = input()
    print(a)
    if a == 'q':
        break;

# 6079 - 언제까지 더해야 할까?
n = int(input())
sum = 0
for x in range(0,1001):
    sum += x
    if sum>=n:
        print(x)
        break

# 6080 - 주사위 2개 던지기
n,m = input().split()
for i in range(1, int(n)+1) :
    for j in range(1, int(m)+1) :
        print(i, j)

# 6081 : [기초-종합] 16진수 구구단 출력하기
a = input()
b = int(a,16)
for i in range(1,16):
    print('%X*'%b,'%X'%i,'=%X'%(b*i),sep='')
# 공백없이 출력하는 방법. sep='' 사용. 얘는 프린트 안에서!
# end=''는 print()를 마치고 엔터안치는거

# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자
a = int(input())
for x in range(1,a+1):
    ans = x
    if x%10 in [3,6,9]:
        ans = 'X'
    print(ans,end=' ')

# 6083 : [기초-종합] 빛 섞어 색 만들기    
r,g,b = map(int,input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
print(r*g*b)

# 6084 : [기초-종합] 소리 파일 저장용량 계산하기
h,b,c,s = map(int,input().split())
print(f'{h*b*c*s/8/1024/1024:.1f} MB')
#f-string! rewind

# 6085 : [기초-종합] 그림 파일 저장용량 계산하기
w,h,b = map(int,input().split())
print(f'{h*b*w/8/1024/1024:.2f} MB')

# 6086 : [기초-종합] 거기까지! 이제 그만~
a = int(input())
sum = 0
number = 0
while True:
    number += 1
    sum += number
    if sum>=a:
        print(sum)
        break

# 6087 : [기초-종합] 3의 배수는 통과(설명)
a = int(input())
for x in range(1,a+1):
    if x%3 == 0:
        continue
    print(x,end=' ')

# 6088 : [기초-종합] 수 나열하기1
a,d,n = map(int,input().split())
a_n = a+(n-1)*d
print(a_n) 

# 6089 : [기초-종합] 수 나열하기2
a,r,n = map(int,input().split())
a_n = a*(r**(n-1))
print(a_n) 

# 6090 : [기초-종합] 수 나열하기3
a,m,d,n = map(int,input().split())
numlist = [a]
for x in range(n):
    numlist.append(numlist[x]*(m)+d)
print(numlist[n-1])

# 6091 : [기초-종합] 함께 문제 푸는 날
a,b,c = map(int,input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)

# 6092 : [기초-리스트] 이상한 출석 번호 부르기1
import sys
input = sys.stdin.readline
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
answer = [0]*23
for j in range(n):
    answer[a[j]-1] += 1
for k in range(23):
    print(answer[k],end=' ')

# 6093 : [기초-리스트] 이상한 출석 번호 부르기2
n = int(input())
a = input().split()
b = list(map(int,a[::-1]))  ## 굿굿
for x in range(len(b)):
    print(b[x],end = ' ') 
#나름 잘풀었다. 위에 문제보다 훨씬 깔끔하게

# 6094 : [기초-리스트] 이상한 출석 번호 부르기3
n = int(input())
a = list(map(int,input().split()))  ##굿굿
a.sort()
print(a[0])

# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기
n = int(input())
pan = []
for i in range(19):
   pan.append([])
   for j in range(19):
       pan[i].append(0)
#기본 바둑판 생성

for _ in range(n):
    x, y = map(int,input().split())
    pan[x-1][y-1] = 1

for i in range(len(pan)):
    for j in range(len(pan[i])):
        print(pan[i][j],end = ' ')
    print()

#6096 : [기초-리스트] 바둑알 십자 뒤집기
#입력 바둑판 생성  
pan = []
for i in range(19):
   x = list(map(int,input().split()))
   pan.append(x)

# x,y행열 뒤집기
n = int(input()) 
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(19):
        if pan[x-1][i] == 0:
            pan[x-1][i] =1
        else:
            pan[x-1][i] = 0
    
        if pan[i][y-1] == 0:
            pan[i][y-1] =1
        else:
            pan[i][y-1] = 0
#2차원 배열 원소 출력
for i in range(19):
    for j in range(19):
        print(pan[i][j],end = ' ')
    print()
# else문 아래에 == 0 했다가 계속 틀려가지고 
# 1시간 동안 고민했다. 오타체크...


# 6097 : [기초-리스트] 설탕과자 뽑기
h,w = map(int,input().split())
n = int(input())
arr = []
for i in range(h):
    arr.append([])
    for j in range(w):
        arr[i].append(0)

for i in range(n):
    l,d,x,y = map(int,input().split())
    for j in range(l):
        if d == 0:
            arr[x-1][y-1+j] =1
        else:
            arr[x-1+j][y-1] =1
for i in range(h):
    for j in range(w):
        print(arr[i][j],end=' ')
    print()
# 아니 첫줄 입력을 왜 거꾸로주고 난리. 입력순서 확인할것!