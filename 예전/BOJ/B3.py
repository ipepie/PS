#1009  진작 런타임 오류나서 규칙찾아야겠구나 하고 찾았는데 모든 테케 다해도 다맞는데
#알고보니까 0번 컴퓨터가 없고 10번컴퓨터라 a%10 == 0 인 경우에 10 하게 해야했다...
ans = []
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    if a%10 in [2,3,7,8]:
        if b%4 == 0:
            ans.append(str(pow(a,4)%10))
        else:
            ans.append(str(pow(a,b%4)%10))
    elif a%10 in [4,9]:
        if b%2 == 0:
            ans.append(str(a*a%10))
        else:
            ans.append(str(a%10))
    elif a%10 == 0:
        ans.append(str(10))
    else:
        ans.append(str(a%10))
print('\n'.join(ans))
#a의 b승은 a**b로 나타낼 수 있다.
#그리고 그냥 4,9처럼 2번 반복 주기도 그냥 4번반복주기 넣어서 해도되네
