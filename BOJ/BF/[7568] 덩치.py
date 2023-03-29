import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x,y))

for i in data:
    ans = 1
    
    for j in data:
        if (i[0]<j[0]) and (i[1] < j[1]):
            ans += 1

    print(ans, end = ' ')
        
