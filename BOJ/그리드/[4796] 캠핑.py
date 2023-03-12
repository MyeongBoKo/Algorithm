import sys
input = sys.stdin.readline

i = 0
while True:
    L, P, V = map(int, input().split())
    if L+P+V == 0:
        break
    else:
        if V % P > L:
            result = ((V//P)*L)+L
        else:
            result = ((V//P)*L)+(V%P)
    i += 1        
    print("Case %d: %d" %(i,result))
