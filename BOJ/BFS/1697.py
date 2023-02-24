import sys
from collections import deque

N, K = map(int, input().split())
max_num = 10**5
visited = [0]*(max_num+1)

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            print(visited[x])
            break

        for i in (x-1, x+1, 2*x):
            if 0<=i<=max_num and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

bfs()
