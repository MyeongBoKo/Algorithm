import sys
input = sys.stdin.readline

n = int(input())
n_arr = sorted(list(map(int, input().split())))

m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2
        ans = False

        if n_arr[mid] > i:
            end = mid - 1
        elif n_arr[mid] < i:
            start = mid + 1
        else:
            ans = True
            break

    if ans == True:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
