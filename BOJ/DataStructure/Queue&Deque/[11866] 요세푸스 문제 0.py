from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = deque([i for i in range(1,N+1)])
ans = []

while arr:
    for _ in range(K-1):
        arr.append(arr.popleft())

    ans.append(arr.popleft())

print('<' + ', '.join(map(str, ans)) +'>')
