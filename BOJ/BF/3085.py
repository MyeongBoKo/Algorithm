n = int(input())

arr = []
for _ in range(n):
    colors = list(map(str, input()))
    arr.append(colors)

maxCnt = 0  


def width():
    global maxCnt 

    for k in range(n):
        countRow = 1
        for l in range(n-1):
            if arr[k][l] == arr[k][l+1]:
                countRow += 1
                maxCnt = max(maxCnt, countRow)
            else:
                countRow = 1

def heigh():
    for k in range(n):
        global maxCnt

        countColumn = 1
        for l in range(n-1):
            if arr[l][k] == arr[l+1][k]:
                countColumn += 1
                maxCnt = max(maxCnt, countColumn)
            else:
                countColumn = 1

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            width()
            heigh()
            arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            width()
            heigh()
            arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]

print(maxCnt)
