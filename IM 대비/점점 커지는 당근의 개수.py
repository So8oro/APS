T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int,input().split()))
    increasing = 1
    max_increasing = 1

    for i in range(N-1):
        if arr[i]<arr[i+1]:
            increasing += 1
            if increasing > max_increasing:
                max_increasing = increasing
            if increasing == 10:
                break
        else:
            increasing = 1

    print(f'#{tc} {max_increasing}')