def recursion(n):
    if n==0:
        return 1
    else:
        return n * recursion(n-1)

n=int(input())
print(recursion(n))

