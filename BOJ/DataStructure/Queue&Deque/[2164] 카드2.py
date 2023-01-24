from collections import deque

N = int(input())
card2 = deque([i for i in range(1, N+1)])

while card2:
    if len(card2) != 1:
        card2.popleft()
        card2.append(card2.popleft())
    else:
        print(card2.pop())
        break
