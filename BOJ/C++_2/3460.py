for _ in range(int(input())):
    n = int(input())
    ans = []
    while (n>0):
        ans.append(n%2)
        n //= 2

    

    for i in range(len(ans)):
        if ans[i] == 1:
            print(i, end = ' ')
