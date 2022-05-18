N = int(input())
for x in range(1,10):
    print(N,'*',x,'=',N*x)


T = int(input())
for _ in range(T):
    A,B= map(int,input().split())
    print(A+B)


n = int(input())
ans = 0
for x in range(1,n+1):
    ans += x
print(ans)

#15552 많은 input을 받을때 처리 시간이 비효율적. input = sys.stdin.readline
#해놓고 input이랑 똑같이 사용하면 효율적. split이나 int도 똑같이 사용가능
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    print(A+B)

import sys
input = sys.stdin.readline
N = int(input())
for i in range(1,N+1):
    print(i)

import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    print(N)
    N = N-1
#아래처럼 range함수를 역순으로 사용가능. 대신 증가폭을 음수로 꼭써줘야함
#import sys
#input = sys.stdin.readline
#N = int(input())
#for i in range(N,0,-1):
#   print(i)

import sys
input = sys.stdin.readline
T = int(input())
for i in range(1,T+1):
    A,B = map(int,input().split())
    print("Case #"+str(i)+":",A+B)
#   print(f'Case #{i}: {A+B}')

#11022
import sys
input = sys.stdin.readline
T = int(input())
for i in range(1,T+1):
    A,B = map(int,input().split())
    print("Case #"+str(i)+":",A,"+",B,"=",A+B)
#   print(f'Case #{i}: {A} + {B} = {A+B}')
#   print('Case #{}: {} + {} = {}'.format(i,A,B,A+B))
#위에 두문제는 format메쏘드나 f-string 사용하면 더 간단
#f-string은 중괄호(객체) 안에 변수를 입력.
#참고로 f스트링은 print(f'{변수:^숫자'}) 처럼 정렬도 가능 ^는 가운데
#숫자자리에는 자료형이 int인 변수 안되고 그냥 무조건 숫자로써야하는듯

#2439
N = int(input())
for i in range(1,N+1):
    print(f'{"*"*i:>{N}}')
#이렇게 하면되네
#f-string 함수는 따옴표 안의 문자는 일반문자열로, {}안의 문자는 변수값으로 출력한다.
#{}안에서 변수를 또 쓰고싶을 때 {}를 한번더 감싸주면되네
#그리고 처음에 f'하고 {}안에서 문자열을 또 쓸때에는 '' "" 다르게 써야함. 순서는 상관없음.


#10871
import sys
input = sys.stdin.readline
N,X = map(int,input().split())
sequence = list(map(int,input().split()))
for i in sequence:
    if i < X:
        print(i,end=' ')
#join안쓰고 프린트 한줄에 출력하기 적용
# sequence = []
# sequence += input().split()
#이렇게 풀었었는데 저렇게 하면 간단하네
N,X = map(int,input().split())
sequence = list(map(int,input().split()))
for i in range(N):
    if X > sequence[i]:
        print(sequence[i], end=' ')
예전이었으면 이렇게 리스트 인덱스로 풀었을듯

#10952
while True:
    A,B = map(int,input().split())
    if A == 0 and B ==0:
        break
    print(A+B)
#무한루프 쓰는법. while True
#강제로 빠져나가려면 break쓰면됨

#10951
while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break
#try에서 처리 못해서 에러나는 부분을 except가 처리

#1110
#int로 풀기
N = int(input())
new = N
ans = 1
while True:
    new = (new%10)*10 + (new//10 + new%10)%10
    if new == N:
        break
    ans += 1
print(ans)

# 문자열로 풀기
N = input()
if int(N)<10:
    N = '0'+ N
new = N
ans = 1
while True:
    new = new[-1] + str(int(new[0])+int(new[-1]))[-1]
    if new == N:
        break
    else:
        ans +=1
print(ans)
#else안써도 된다. 어차피 while문 안에서 ans +=1 을 처리함.
#또 풀어보면 좋을듯 나중에
#십의자리랑 일의자리 먼저 따로 계산해놓고 간단하게 써도될듯.
