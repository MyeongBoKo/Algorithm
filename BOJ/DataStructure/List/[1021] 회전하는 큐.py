from collections import deque

N, M = map(int, input().split())
circle = deque([i for i in range(1,N+1)])
idx = list(map(int, input().split()))

count = 0
for i in idx:
    while True:
        if circle[0] == i:
            circle.popleft()
            break
        else:
            if circle.index(i) < len(circle)/2:
                while circle[0] != i:
                    circle.append(circle.popleft())
                    count += 1
            else:
                while circle[0] != i:
                    circle.appendleft(circle.pop())
                    count += 1

print(count)
                    
