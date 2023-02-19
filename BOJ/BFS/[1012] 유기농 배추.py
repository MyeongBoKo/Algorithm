from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[x][y] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                

T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[0]*(M) for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)

                
    
