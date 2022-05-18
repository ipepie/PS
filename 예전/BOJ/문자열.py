#1157
import collections
word = input().upper()
n = collections.Counter(word).most_common()
if len(n) == 1:
    print(word)
elif n[0][1] == n[1][1]:
    print('?')
else:
    print(n[0][0])

#10809
S = input()
alpha = list('abcdefghijklmnopqrstuvwxyz')
for x in alpha:
    print(S.find(x),end=' ')
#알파벳을 list(range(97,123))으로 해도됨. 아스키코드 숫자범위임
#chr(97) = 'a' 니까 print(S.find(chr(x))) 하면됨

#2675
T = int(input())

for i in range(T):
    R,S = input().split()
    P = ''
    for i in S:
        P += int(R)*i
    print(P)

#2908
a,b = input().split()
n_a = int("{}{}{}".format(a[2],a[1],a[0]))
n_b = int("{}{}{}".format(b[2],b[1],b[0]))
print(max(n_a,n_b))
#다른방법1
#list(reversed(a)) 하면 순서뒤집을수있음. 한다음 join하면 뒤집은 문자열
#다른방법2. 슬라이싱이용
#A = int(A[::-1])
#B = int(B[::-1])
# A[::-1] == A[-1:-4:-1]  같은 표현입니다.
# 첫끝부터 시작해서, 첫글자까지 즉, 글자를 거꾸로 돌립니다.

#5622
a = list(input())
b = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for i in a:
    for j in b:
        if i in j:
            time += b.index(j) +3
print(time)

#2941
change = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
for i in change:
    a = a.replace(i,' ')
print(len(a))

#1316
N = int(input())
word = []
ans = 0
for i in range(N):
    word.append(input())
for x in word:
    for y in range(len(x)):
        if x.count(x[y]) == x.rfind(x[y]) - x.find(x[y]) + 1 :
            x1= x[y+1:]
            if x1 == '':
                ans += 1
        else:
            break
print(ans)
#와 이렇게 푸는사람 나밖에 없을듯..
#for x in range(len(x))하면 인덱스로 풀 때 x x+1이 인덱스초과할까봐 걱정했는데
# for x in word:
#    for y in range(len(x)-1):
#        if x[y] == x[y+1]:
#이런식으로 range 하나 줄이면 됐네
#그다음 조건식으로 word의 문자갯수 set써서 구하고 인접한 문자가 다를때 변수하나 +=1
#해서 개수가 같으면 그룹 단어로. ans +1. ans출력
#내가 푼 문자열 슬라이싱에서는 인덱스 초과해도 오류안나니까 가능. 빈문자열나옴
