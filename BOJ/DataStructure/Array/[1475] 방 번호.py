n = input()
count = [0]*10

for i in n:
    if i == '9' or i == '6':
        if count[6] == count[9]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[int(i)] += 1

print(max(count))
