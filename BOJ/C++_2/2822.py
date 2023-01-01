score = []
for i in range(8):
    score.append(int(input()))
num_ = []
answer = 0
for i in range(5):
    answer += max(score)
    num_.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
num_.sort()
print(answer)
print(*num_)
