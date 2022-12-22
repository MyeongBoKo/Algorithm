import sys
input = sys.stdin.readline

N=int(input())
data = [input().rstrip() for _ in range(N)]

result = ""

def solution(x,y,N):
    global result
    num = data[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if data[i][j] != num:
                result += '('
                solution(x,y,N//2)
                solution(x,y+N//2,N//2)
                solution(x+N//2,y,N//2)
                solution(x+N//2,y+N//2,N//2)
                result += ')'
                return

    if num == 0:
        result += '0'
    else:
        result += '1'
    return

solution(0,0,N)
print(result)
                
