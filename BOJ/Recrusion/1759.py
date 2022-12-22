def solution(start, result, vowel, consoant):
    if len(result)==L and vowel>=1 and consoant>=2:
            print(''.join(result))
            return

    for i in range(start, C):
        if alpha[i] in vowels:
            solution(i+1, result+list(alpha[i]), vowel+1, consoant)
        else:
            solution(i+1, result+list(alpha[i]), vowel, consoant+1)

    
L, C = map(int,input().split())
alpha = list(map(str, input().split()))
alpha.sort()
vowels = ['a','e','i','o','u']
result = []

solution(0, result, 0, 0)
