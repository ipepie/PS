# 백준 2580 스도쿠
# 22/6/8
# 백트래킹
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
graph = []
for i in range(9):
    graph.append(list(map(int,input().split())))

# 0의 위치 저장
blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

# 해당 칸에 올 수 있는 숫자인지 체크 함수
# n이 후보값
def check(x,y,n):
    # 가로 줄 중복체크
    if n in graph[x]:
        return False
    # 세로 줄 중복체크
    for i in range(9):
        if n == graph[i][y]:
            return False
    # 3x3 한칸 내 중복체크
    nx = x//3
    ny = y//3
    for i in range(3):
        for j in range(3):
            if n == graph[3*nx+i][3*ny+j]:
                return False
      
    return True

def dfs(idx):
    # blank안에 있는 0 개수만큼 dfs 
    if idx == len(blank):
        for ans in graph:
            print(*ans)
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if check(x,y,i):
            graph[x][y] = i
            dfs(idx+1)
            # 다시 0으로 바꿔서 나머지 i범위도 탐색 하도록
            graph[x][y] = 0

dfs(0)

# 0으로 도배된 테케에서 제대로 동작 안함.
# 그냥 앞에서부터 x가 되는대로 바로 들어가서 뒤에가서 check = False 인 경우가 생겨 0이 그대로 남게되는데
# 이때 돌아가는 걸 구현하기가 애매함.
# 처음부터 0인 xy좌표 저장해서 하는걸로 바꿈

# def dfs(row):
#     if row == 9:
#         return
#     for x in range(9):
#         if graph[row][x] == 0:
#             for n in range(1,10):
#                 if check(row,x,n):
#                     graph[row][x] = n
#                     break
#     dfs(row+1)

                    
