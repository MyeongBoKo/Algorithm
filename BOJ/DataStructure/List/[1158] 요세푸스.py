from collections import deque

n,k = map(int, input().split())
circle = deque(range(1, n+1))
ans = []

for i in range(n):
    for j in range(k-1):
        circle.append(circle.popleft())
    ans.append(circle.popleft())

print('<'+', '.join(map(str,ans))+'>')
    
