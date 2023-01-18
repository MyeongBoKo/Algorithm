import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
circle =deque(enumerate(map(int, input().split())))

for i in range(n):
    p = circle.popleft()
    print(p[0]+1, end= ' ')
    if p[1]>0:
        circle.roate(-(p[1]-1))
    else:
        circle.roate(-(p[1]))
