def BinaryInprint(n):
    if n<2:
        print(n, end='')
    else:
        BinaryInprint(n//2)
        print(n%2, end='')

n = int(input())
BinaryInprint(n)
        


        
