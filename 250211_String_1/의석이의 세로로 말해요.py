T = int(input())

for tc in range(1,T+1):

    arr = [list(input()) for _ in range(5)]

    print(f'#{tc}', end=' ')

    for j in range(15):
        for i in range(5):
            if j<len(arr[i]):
                print(arr[i][j], end='')

    print()
