n = int(input())
arr = []
for _ in range(n):
    color = list(map(str,input()))
    arr.append(color)

countMax = 0

def row():
    global countMax
    
    for i in range(n):
        countRow = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                countRow += 1
                countMax = max(countMax, countRow)
            else:
                countRow = 1
                
def heigh():
    global countMax
    
    for i in range(n):
        countColumn = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                countColumn += 1
                countMax = max(countMax, countColumn)
            else:
                countColumn = 1
                
                
for i in range(n):
        for j in range(n-1):
            if arr[i][j] != arr[i][j+1]:
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                row()
                heigh()
                arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
            if arr[j][i] != arr[j+1][i]:
                arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
                row()
                heigh()
                arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]
    
print(countMax)        
