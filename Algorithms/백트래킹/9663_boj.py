# 백준 9663 N-Queen
# 22/6/2
# 백트래킹. 재귀

# python3은 시간초과, pypy3은 성공
n = int(input())
graph = [0] * n

cnt = 0

def dfs(status):
    global cnt
    if status == n:
        cnt += 1
        return

    for i in range(n):
        graph[status] = i
        if is_promising(status):
            dfs(status+1)

def is_promising(status):
    for i in range(status):
        # 열이 같거나 대각선에 있는 경우 제외
        # 행은 status, 열은graph[status]
        # 대각선은 x좌표의 차와 y좌표의 차의 절대값이 일치하는지 여부 확인으로 체크
        if graph[i] == graph[status] or abs(status-i) == abs(graph[status]-graph[i]):
            return False
    return True
dfs(0)
print(cnt)