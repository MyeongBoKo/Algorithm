c = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    c_input = input().split()
    for j in range(19):
        d[i+1][j+1] = int(c_input[j])

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    for j in range(1, 20):
        if d[j][y] != 0:
            d[j][y] = 0
        else:
            d[j][y] = 1

        if d[x][j] != 0:
            d[x][j] = 0
        else:
            d[x][j] = 1

for i in range(1, 20):
    for j in range(1,20):
        print(d[i][j], end= ' ')
    print()
    
