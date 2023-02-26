from collections import deque

N = int(input())
q = deque([i for i in range(1,N+1)])
ans = []

while q:
    if len(q) != 1:
        ans.append(q.popleft())
        q.append(q.popleft())
    else:
        ans.append(q.pop())
        print(*ans)
        break
