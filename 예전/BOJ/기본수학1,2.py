#2292
import sys
input = sys.stdin.readline
N = int(input())

bn
6 12 18 24
S_bn = 2/n(12+ (n-1)*6)
(3n+3)n
S_bn-1 = 3n(n-1) = 3*n*n-3n
수열 An (1 7 19 37 61)
계차수열. An의 일반항을 구하고 인풋N이 n번째에 속해있는지 확인
3번째 즉. 8~19 사이의 수라면 n =2 < N < n+1=3 니까 while 루프의 n+1출력
점화식 고민하고 n하나씩 증가시키면서 어디 속해있는지 확인하는 코드 작성
N = int(input())
n = 1
while True:
    if N == 1:
        print(1)
        break
    elif N >= 1 + 3*n*n-3*n and N <= 1 + 3*(n+1)*(n+1)-3*(n+1):
        print(n+1)
        break
    else:
        n += 1

N = int(input())
A = 1
B = 6
room_number = 1
if N ==1 :
    print(1)
else:
    while True:
        A+= B
        room_number += 1
        if N<=A:
            print(room_number)
            break
        B+=6
#이게 점화식 안쓰고 훨씬 간단하네 그냥 계차 그때그때 늘려주고 An을 만드는거

#1193
X = int(input())
count = 0
while X > 0:
    count += 1
    X -= count
n = abs(X)
arr = list(range(1,count+1))
brr = arr[::-1]

if count % 2 != 0:
    print('%d/%d'%(arr[n],brr[n]))
else:
    print('%d/%d'%(brr[n],arr[n]))
#다른 사람들 풀이 다들 다르고 이해하기 어려웠다.
#대각선으로 1 2 3 4 5 개씩 있는 걸로 접근은 맞았는데
#인풋X에 1 2 3 4 5 ... 씩 빼면서 몇째줄에 있는지 확인하고
#N번째 줄에서 가장큰 분모분자는 N이니 1부터N까지 range로 리스트 뽑고
#abs로 그게 0에서 부터 얼마나 떨어져있는지. 인덱스값으로 활용해서 끝..
#다시 풀래도 못풀겠다

#2869
A,B,V = map(int,input().split())
if (V-A) % (A-B) == 0:
    print(int((V-A) / (A-B))+1)
else:
    print(int((V-A) / (A-B))+2)
# a,b,v = map(int,input().split())
# k = (v-b)/(a-b)
# print(int(k) if k == int(k) else int(k)+1)

#10250
T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    x = 0  # 호
    y = 0  # 층

    if N % H == 0:
        x = N // H
        y = H * 100
    else:
        x = N // H + 1
        y = N % H * 100
    print(y+x)
# if N//H<10:
#      print(Y+'0'+X)
# else:
#      print(Y+X)
# 나는 문자열로 생각해서 또 if절 쓰고 0추가했는데 숫자로 하면 저렇게되구나

#2775
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    f0 = list(range(1,n+1))
    for x in range(k):
        for y in range(1,n):
            f0[y] += f0[y-1]
    print(f0[-1])

0층 1,2,3,4,5,6 ... n호 = n명
1층 1,3,6,10,15,16
2층 1,4,10,20,35,51
3층 1,5,15,35,70,121
k층의 n호.. 앞방과 아랫방 더하면되는군.

#2839
n = int(input())
a = n//5
b = n//3
ans = []
for i in range(a+1):
    for j in range(b+1):
        if i*5 + j*3 == n:
            ans.append(i+j)
if ans == []:
    print(-1)
else:
    print(min(ans))

# n = int(input())
#
# result = n // 5
#
# for i in range(result, -1, -1):
#     k = n - (i * 5)
#     if k % 3 == 0:
#         result += k // 3
#         break
#     else:
#         result -= 1
#
# print(result)
#이렇게 해도되네. n 5로나눈 몫을 하나씩 줄여갔을 때 3으로 나누어떨어지는지 확인

n = int(input()) # 설탕

result = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
        print(-1) # while문이 거짓이 되면 -1 출력
#원래 이방식을 생각했는데 if n%3까지 생각해서 머리터져서 실패

#10757
a,b = map(int,input().split())
print(a+b)

#1011
T = int(input())
ans = 1
for i in ragne(T):
    x,y = map(int,input().split())
    for j in range(1,y-x):
        ans += 1
        if ans == y-x-1:
            print(ans)
#다시풀것

#기본 수학2
#1978
에라토스테네스의 체..
공부전
N = int(input())
number = list(map(int,input().split()))
era = set(range(2,1001))
ans = 0
for i in era:
    while i**2>= 1000:
        for j in range(2,1001):
            if j != i:
                era.discard(j)
for x in number:
    if x in era:
        ans += 1
print(ans)

에라토스테네스의 체 구현
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

딱봐도 while문에서 너무오래걸릴거같다.
N = int(input())
number = list(map(int,input().split()))
arr = [True]*N
arr[0] = False
for i in range(N):
    for j in range(2,int(**0.5)+1):
        if arr[i] == True:
            for k in range(i+1,N,i):
                arr[k] = False
print(arr)

아 뭔가 디럽게 이상하네 아직 이해가 안된다. 이문제는 안써도되니까 안쓰는식으로 다시
N = int(input())
number = list(map(int,input().split()))
ans = 0
for i in number:
    p = 0
    if i == 1:
        continue
    for j in range(2,i+1):
        if i%j == 0:
            p += 1
    if p == 1:
        ans += 1
print(ans)


#2581 또 소수
m = int(input())
n = int(input())
prime_list = []
for i in range(m,n+1):
    p = 0
    if i ==1:
        continue
    for j in range(2,i+1):
        if i%j == 0:
            p += 1
    if p == 1:
        prime_list.append(i)
if prime_list == []:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])
    #print(min(prime_list))
#min을 하면 배열이 엄청길때 다확인해서 작은걸 출력해서 시간초과가떴다
#첫번째인덱스가 제일 작으니까 해결

#11653
n = int(input())
if n == 1:
    pass
else:
    for i in range(2,n+1):
        while True:
            if n%i == 0:
                print(i)
                n = n//i
            else:
                break
#시간이 개빡세게 걸리긴했는데 정답은 맞음..
n=int(input());i=2
while n>1:
 if n%i:i+=1
 else:n//=i;print(i)
 이게 숏코딩인데. 최소 소수 2 지정하고 하나씩 올리는게 문제 방향성이랑 맞지 않다고 생각했다...
 이렇게 하면 for문 안쓰고 할수는 있네.

더쉬운방법
N = int(input())
number = 2

while N != 1:
    if N % number == 0:
        print(number)
        N = N // number
    else:
        number += 1
이게 나랑 비슷하고 이해하기 쉬운듯

#1929 또 또 소수
m,n = map(int,input().split())
for i in range(m,n+1):
    p = 0
    for j in range(2,i+1):
        if i%j == 0:
            p += 1
    if p == 1:
        print(i)
처음 답 시간초과!!!

m,n = map(int,input().split())
prime = [True] * (n+1)   # ==  [True for i in range(n+1)]
for i in range(2,n+1):
    if prime[i] == True:
        if i >=  m:
            print(i)
        for j in range(i*2,n+1,i):
            prime[j]= False
#에라토스 테네스의 체랑 비슷한데 그건 변수 하나만 받아서
#처음 for 문에서 int(n**i)+1로 가장큰 약수인 루트까지만 돌렸지만
#여기선 끝까지 돌려야 하는듯.
#그냥 체 돌리고 마지막에 range(m,n+1) 에서 True인것만 뽑아서 출력해도 될듯


#4948 베르트랑 공준. 또 소수
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
while True:
    a = int(input())
    if a == 0:
        break
    print(len(prime_list(2*a+1))-len(prime_list(a+1)))
#에라토스테네스의 체 함수 긁어와서 사용했음.
#근데 밑에처럼 문제 N 범위 있으니까
is_prime = [1]*246913
is_prime[0] = is_prime[1] = 0
# 1 ~ 123456
for i in range(2, int(246912**0.5)+1):
    if is_prime[i] == 1:
        for j in range(i*2, 246913, i):
            is_prime[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(is_prime[n+1:n*2+1]))
이렇게 전체 N 범위 체 걸러놓고 인풋n가지고 하면될듯
이게 더 좋은거같다. 직접 에라토스테네스 체 구현해봐야 늘듯.

#9020
T = int(input())
prime = [1] * 10001
prime[0] = prime[1] = 0
for i in range(2,int(10001**0.5)+1):
    if prime[i] == 1:
        for j in range(i+i,10001,i):
            prime[j] = 0
        prime[i] = i
p = [x for x in prime if x != 0]
ans = []
for k in range(T):
    n = int(input())
    for x in p:
        if n-x in p and x<=n-x:
            ans.append([x,n-x])
    print(ans[-1][0],ans[-1][1], end = ' ')
와 어떻게 생각한대로 잘 풀긴 했는데 역시 시간초과!
마지막 for문을 수정해보면될거같은데 모든소수가아니라 round(n/2)정도
풀이 참고 및 수정

T = int(input())
prime = [1] * 10001
prime[0] = prime[1] = 0
for i in range(2,int(10001**0.5)+1):
    if prime[i] == 1:
        for j in range(i+i,10001,i):
            prime[j] = 0
p = [x[0] for x in enumerate(prime) if x[1] != 0]
# p = [i for i, j in enumerate(prime_ox) if j == True and i >=2 ] 랑 똑같다
# 여기까지 에라토스테네스의 체 공통부분 p는 그중에서 소수만 리스트 뽑은거
for _ in range(T):
    n = int(input())
    for k in range(n//2,1,-1):
        if k in p and n-k in p:##
            print(k,n-k)
            break
#지렸다 반갈라서 하나씩 줄여가면서 두 수가 모두 소수인지 확인
#굳이 소수 뽑은 리스트 안에서 하나씩 더해볼 필요가 없
# 소수뽑은리스트 p안쓰고 0부터 10001까지 prime 리스트만 사용하면
# ##부분에서 if prime(k) and prime:  으로 사용가능 ==1 True 뜻이니까

 
