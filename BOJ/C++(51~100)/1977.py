import math

def check():
    for i in range(result[0], result[1]+1):
        if i%(math.sqrt(i))==0:
            ans.append(i)

    if (len(ans) == 0):
        print(-1)
    else:
        print(sum(ans))
        print(min(ans))



result = [int(input()) for _ in range(2)]
ans = []
check()
