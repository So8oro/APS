T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int,input().split()))

    min_diff = 200
    idx = 0

    for i in range(N-1):
        fir_worker = 0
        sec_worker = 0
        for j in range(i+1):
            fir_worker += arr[j]
        for k in range(i+1,N):
            sec_worker += arr[k]
        if min_diff > abs(fir_worker-sec_worker):
            min_diff = abs(fir_worker-sec_worker)
            idx = i+1



    print(f'#{tc} {idx} {min_diff}')