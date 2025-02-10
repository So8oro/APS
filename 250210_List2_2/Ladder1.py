for _ in range(10):

    tc = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]

    for j in range(100):
        if arr[99][j] == 2:
            j_idx = j       # 도착 위치의 j 값을 찾아서 기록해두었다.
            break

    for i in range(99, -1, -1):     # 마지막 행에서부터 차례대로 올라가서 맨 위까지 보도록 하자
        for nj in range(1,100):     # 현재 위치에서 좌우를 탐색하자.
            if 0<=j_idx-1<100 and arr[i][j_idx-1]:    # 좌측을 보자. 인덱스 내에 있고, 값이 1인가?
                arr[i][j_idx] = 0
                j_idx -= 1                              # 그곳으로 옮겨가자.
            elif 0<=j_idx+1<100 and arr[i][j_idx+1]:    # 아니라면 우측을 보자.
                arr[i][j_idx] = 0
                j_idx += 1                              # 조건이 충족되면 옮겨가자.
            else:
                break       # 양쪽 다 0이라면 좌우 탐색 중지. 다음 행으로 올라가자.

            '''
            근데 좌우 탐색을 쭉 해야한다. 0을 만날 때까지! 지금은 0을 만나도 뒤돌아갈 뿐인데 어찌할 것인가?
            1. 좌측을 보고 간다면, 그쪽으로 쭉 가자.
            2. 우측을 보고 간다면, 그쪽으로 쭉 가자.
            3. 그럼 좌우를 판단한 이후에 for 문을 돌려보자.
            
            더 좋은 방법! 지우면서 가자. 지나간 길을 0으로 만들자.
            '''

    print(f'#{tc} {j_idx}')