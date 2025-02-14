T = int(input())

for tc in range(1,T+1):

    sqr1 = list(map(int,input().split()))
    sqr2 = list(map(int,input().split()))

    # 만나는 부분이 없는 경우를 먼저 확인하자.

    # 1보다 2가 우측 / 1보다 2가 좌측 / 1보다 2가 위쪽 / 1보다 2가 아래
    if sqr1[2] < sqr2[0] or sqr1[0] > sqr2[2] or sqr1[3] < sqr2[1] or sqr1[1] > sqr2[3]:
        result = 4

    # 점에서 만나는가?
    # 1의 1,2,3,4(우상부터 시계방향) 꼭짓점이 2의 3,4,1,2와 일치하는가
    # 1:23  2:03  3:01  4:21
    elif (sqr1[2],sqr1[3])==(sqr2[0],sqr2[1]) or (sqr1[0],sqr1[3])==(sqr2[2],sqr2[1]) or \
            (sqr1[0],sqr1[1])==(sqr2[2],sqr2[3]) or (sqr1[0],sqr1[3])==(sqr2[2],sqr2[3]):
        result = 3

    # 점에서 만나지 않는데 좌표가 일치한다면 선에서 만나는 것이다.
    # 하지만, 선에서 만나면서 안에 있는 것이 아닌지 체크를 해야한다!!!
    elif (sqr1[2]==sqr2[0] and sqr1[2]<sqr2[2]) or (sqr1[3]==sqr2[1] and sqr1[3]<sqr2[3]) or \
            (sqr1[0]==sqr2[2] and sqr1[2]>sqr2[2]) or (sqr1[3]==sqr2[3] and sqr1[3]>sqr2[3]):
        result = 2

    # 전부 아니라면, 겹치는 것이다.
    else:
        result = 1



    print(f'#{tc} {result}')