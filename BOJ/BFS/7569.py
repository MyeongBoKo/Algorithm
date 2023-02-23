import sys
from collections import deque

M, N, H = map(int, input().split())

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

q = deque()
answer = 0

def bfs():
    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if -1 < nx < M and -1 < ny < N and -1 < nz < H:
                q.append((nz, ny, nx))
                graph[nz][ny][nx] = graph[z][y][x] + 1
                visited[nz][ny][nx] = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1 and not visited[i][j][k]:
                q.append((i,j,k))
                visited[i][j][k] = True

bfs()

for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer-1)


