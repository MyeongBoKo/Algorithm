import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(x, y):
    visited[x][y] = 1

    

    if graph[x][y] == 1:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<N) and (0<=ny<M):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx,ny)
    

    

while True:
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        break

    graph = []
    visited = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(N):
        graph.append(list(map(int,input().split())))


    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
            else:
                continue
                
                

    print(cnt)
                
