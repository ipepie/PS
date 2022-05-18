A, B = map(int,input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')

score = int(input())
if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('F')

year = int(input())
if year%4 == 0 and (year%100 !=0 or year%400 ==0):
    print(1)
else:
    print(0)

x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)

N = int(input())
pattern = list(input())
for x in range(N-1):
    file = list(input())
    for y in range(len(pattern)):
        if pattern[y] != file[y]:
            pattern[y] = "?"

#1157번 시간초과 답 ㅠㅠ 딕셔너리 반복이 오래걸리는듯
word = input().upper()
n = {}
for x in word:
    n[x] = word.count(x)
a = list(n.items())
a.reverse()
if a[0][1] == a[1][1]:
    print('?')
else:
    print(a[0])

#set도 중복제거 할 수 있다는데 그냥 내장함수로 해결해봄
#위에서 먼저 set(word)로 중복제거한 후에 하면되려나
import collections
word = input().upper()
n = collections.Counter(word).most_common()
if n[0][1] == n[1][1]:
    print('?')
else:
    print(n[0][0])
#인풋 단어가 1글자일 때 인덱스사용에서 오류 발생하여 수정
import collections
word = input().upper()
n = collections.Counter(word).most_common()
if len(n) == 1:
    print(word)
elif n[0][1] == n[1][1]:
    print('?')
else:
    print(n[0][0])


#1152
sen = input().split()
print(len(sen))

a,b = map(int(),input().split())
print(a//b,'\n',a%b)


#1550 8진수든 16진수든 어떤 수와 해당 진수를 입력해서 이를 10진수로 입력. int함수사용
# int 함수는 특정 진수를 10진수로 바꿔준다.
print(int(input(),16))

A = int(input())
B = int(input())
print(A+B)
print(A-B)
print(A*B)

num = map(int,input().split())
a = 0
for x in num:
    a += x*x
print(a%10)

A = int(input())
B = int(input())
print(A+B)

#2845  프린트 출력 방식 바꾸기. 엔터 없이 출력되게 하는방법. ''안에 아무문자나 가능
L, P = map(int,input().split())
A = L*P
news = map(int,input().split())
for x in news:
    print(x-A,end=" ")

# 반올림은 round(N,자릿수(2로하면 둘째자리까지나옴))함수 사용
# 올림, 내림, 버림은 import math에서 math.ceil floor trunc (N) 으로 사용

#2914
A, I = map(int,input().split())
print(A * (I-1)+1)

#3003
arr = list(map(int,input().split()))
base = [1,1,2,2,2,8]
ans = []
for x in range(len(base)):
    ans.append(str(base[x]-arr[x]))
print(' '.join(ans))
#print(" ".join(str(b-a) for a,b in zip(arr,arr2)))
#zip함수를 이용하면 하나씩 짝지어주는구나
#[str(b-a) for a,b in zip(arr,base)] 로 이해하면될듯

#3046
R1, S = map(int,input().split())
print(2*S-R1)

#5522 for문을 돌리고 싶을 때 변수는 필요없으면 _로 쓰나보다
sum = 0
for _ in range(5):
    sum += int(input())
print(sum)


#5554
sum=0
for _ in range(4):
    sum += int(input())
print(sum//60)
print(sum%60)

#6749
y = int(input())
m = int(input())
print(2*m-y)

#1297
import math #from math import sqrt 하면 함수쓸때 sqrt만해도됨
D, H, W = map(int,input().split())
x= math.sqrt(D*D/(W*W+H*H))
print(math.floor(H*x),math.floor(W*x))
#내림 안쓰고 그냥 int하면 소수점말고 정수만나옴

#1712 손익분기점
A,B,C = map(int,input().split())
if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))


#2420
a, b = map(int, input().split())
if a*b > 0:
    print(abs(a-b))
else:
    print(abs(a)+abs(b))


#2480
money = 0
a,b,c = map(int,input().split())
if a==b==c:
    money = 10000 + a*1000
elif a==b or a==c:
    money = 1000 + a*100
elif b==c:
    money = 1000 + b*100
else:
    money = max(a, b, c)*100
print(money)

#2525
a, b = map(int, input().split())
c = int(input())
if b +c <60:
    print(a,b+c)
elif (b+c)//60+a >=24:
    print((b+c)//60+a-24,(b+c)%60)
else:
    print((b+c)//60+a,(b+c)%60)
# if문돌리기전에 분을 먼저 합쳐놓으면 더 간단해질듯

#2752
a= sorted(list(map(int,input().split())))
for x in range(3):
    a[x] = str(a[x])
print(' '.join(a))
#와. 앞으로 그냥 print end 써야겠다 맨날 리스트 속 정수 추출할때 for문돌려서
#하나씩 문자열로 바꾼다음에 join했는데
#for i in n:
#    print(i,end=' ')

#5543
burger = []
drink = []
money = 3950
for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    drink.append(int(input()))
for x in burger:    #여기서 for문을 돌리지 말고 위에 for문에서
    for y in drink: #각자 최대값인 2000이랑 min돌리면서 가장 작은값하고 밑에서 두개 더해도될듯
        if x+y-50 < money:
            money = x+y-50
print(money)
#아니면 버거 드링크 리스트만 해놓고 min변수로 리스트 가져와도됨. 마찬가지로 마지막 포문중첩생략
# print(min(burger)+min(drink)-50)

#10039
score = []
ans = 0
for _ in range(5):
    score.append(int(input()))
for x in score:
    if x<40:
        ans += 40
    else:
        ans += x
print(int(ans/5))
#import numpy하면 numpy.mean(배열)가능
#sum함수도 리스트 가능.

#10797
day = int(input())
car = map(int,input().split())
ans = 0
for x in car:
    if x == day:
        ans += 1
print(ans)

#연세대학교
N = int(input())
if N == 0:
    print('YONSEI')
else:
    print('Leading the Way to the Future')

#20499
K,D,A = map(int,input().split('/'))
if K+A<D or D ==0:
    print('hasu')
else:
    print('gosu')
