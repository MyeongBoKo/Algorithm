from collections import deque

N = int(input())
deq = deque([i for i in range(1, N+1)])

while len(deq) != 1:
    deq.popleft()
    deq.rotate(-1)

print(deq.pop())





