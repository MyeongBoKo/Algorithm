answer = [0]*1001
triangleNum = [n*(n+1)//2 for n in range(1, 45)]

for i in triangleNum:
    for j in triangleNum:
        for k in triangleNum:
            if i+j+k <= 1000:
                answer[i+j+k] = 1

T = int(input())
for _ in range(T):
    print(answer[int(input())])
