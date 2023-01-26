import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<M) and (0<=ny<N):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

T = int(input())

for i in range(T):
    M, N, K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    ans = 0

    for j in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for m in range(M):
        for n in range(N):
            if graph[n][m] == 1:
                dfs(m, n)
                ans += 1


    print(ans)
                
    
