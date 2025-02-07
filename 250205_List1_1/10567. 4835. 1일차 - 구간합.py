T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int,input().split())
    numlist = list(map(int, input().split()))

    # 첫번째 구간의 합을 우선 구한다
    partsum = 0

    for m in range(M):
        partsum += numlist[m]

    # 최소 최대 구간합 초기화
    maxsum = partsum
    minsum = partsum

    # 구간의 총 개수는 N-M+1
    for m in range(0, N-M):
        partsum -= numlist[m]
        partsum += numlist[M+m]
        if partsum > maxsum:
            maxsum = partsum
        if partsum < minsum:
            minsum = partsum

    print(f'#{test_case} {maxsum-minsum}')