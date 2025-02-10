T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int,input().split()))
    result = [0]*N

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(N//2):
        result[i*2+1] = arr[i]

    for i in range(-1, -N//2-1, -1):
        # -1은 0으로, -2는 2로, -3은 4로 가야함
        result[-(i+1)*2] = arr[i]

    # 아 10개까지 출력이구나...
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()