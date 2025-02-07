T = int(input())

for tc in range(1,T+1):
    L = int(input())
    arr = list(map(int,input()))

    result = 0
    temp_result = 0

    for i in range(L):                  # 하나씩 살펴봅니다
        if arr[i] == 1:                 # 1을 찾으면, 셉니다!
            temp_result += 1
            if temp_result > result:    # 지금까지 센 1의 개수가 최대치라면 갱신합니다. 그리고 다음 요소를 살펴보러 갑니다.
                result = temp_result
        else:                           # 0을 찾았습니다.
            temp_result = 0             # 1개수를 0으로 되돌리고 다시 다음 요소를 살펴보러 갑시다.

    print(f'#{tc} {result}')