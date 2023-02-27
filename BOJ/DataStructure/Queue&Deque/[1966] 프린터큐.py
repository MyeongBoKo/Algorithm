from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    q = deque(list(map(int,input().split())))
    count = 0

    while q:
        num = max(q)
        flag = q.popleft()
        m -= 1

        if num == flag:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            q.append(flag)
            if m < 0:
                m = len(q)-1
