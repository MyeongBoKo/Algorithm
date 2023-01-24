from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    
    if command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    
    if command[0] == 'size':
        print(len(queue))

    if command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
