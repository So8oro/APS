T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    min_diff = N    # 초기값은 가능한 최대치를 초과하는 값으로 설정

    # 크기순으로 정렬된 당근을 세 가지로 나눈다.
    # 셋으로 나누기 위한 두 구분점을 설정한다.
    for i in range(N-2):
        for j in range(i+1,N-1):
            small = i+1
            middle = j-i
            large = N-j-1

            # 같은 종류가 같은 박스에 담겼는지 체크한다.
            if arr[i]!=arr[i+1] and arr[j]!=arr[j+1]:
                diff = max(small,middle,large)-min(small,middle,large)
                if diff < min_diff:
                    min_diff = diff
    if min_diff==N:
        min_diff = -1       # min 값이 아직도 N 이라면, 같은 종류가 같은 박스에 담긴 적이 없다는 것. -1을 출력한다.

    print(f'#{tc} {min_diff}')