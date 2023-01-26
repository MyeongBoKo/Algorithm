import sys
sys.setrecursionlimit(10**7)

N,M,K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1]=1

def dfs(x,y):
    global num
    num += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx,ny)

    return num

ans = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == False:
            num = 0
            dfs(i,j)
            ans = max(ans, num)

print(ans)
