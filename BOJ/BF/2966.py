Adrian = ['A','B','C']*40
Bruno = ['B','A','B','C']*30
Goran = ['C','C','A','A','B','B']*20

N=int(input())
alphabet = list(input())

A_cnt = B_cnt = G_cnt = 0

for i in range(N):
    if alphabet[i] == Adrian[i]:
        A_cnt += 1
    if alphabet[i] == Bruno[i]:
        B_cnt += 1
    if alphabet[i] == Goran[i]:
        G_cnt += 1

max_answer = max(A_cnt, B_cnt, G_cnt)

print(max_answer)

if max_answer == A_cnt:
    print('Adrian')
if max_answer == B_cnt:
    print('Bruno')
if max_answer == G_cnt:
    print('Goran')


