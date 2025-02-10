T = int(input())

for tc in range(1, T+1):

    result = []

    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1):  # 정렬 구간의 시작 인덱스
        min_idx = i # 첫 원소를 최소로 가정
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:  # 최소 원소 위치 갱신
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 구간 최솟값을 구간 맨 앞으로

    print(f'#{tc}', end=' ')
    for i in range(N):
        print(arr[i], end=' ')
    print()