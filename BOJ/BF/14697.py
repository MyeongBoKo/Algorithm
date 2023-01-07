A, B, C, N = map(int, input().split())

res = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            if A*a+B*b+C*c==N:
                res = 1
if res == 1:
    print(1)
else:
    print(0)
