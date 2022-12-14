import sys, heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(n), n))
