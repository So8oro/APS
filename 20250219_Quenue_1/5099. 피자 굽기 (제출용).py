T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    oven = [[-1,-1]]*10000
    front,rear = -1,-1
    last = -1

    for num,cheese in enumerate(pizza):
        if num < N:
            rear += 1
            oven[rear] = [num,cheese]
        else:
            break

    next = N

    for _ in range(1000):

        front += 1
        oven[front][1] //= 2
        if oven[front][1]==0:
            last = oven[front][0]
            rear += 1
            if next<M:
                oven[rear] = [next,pizza[next]]
                next += 1
        else:
            rear += 1
            oven[rear] = oven[front]

    print(f'#{tc} {last+1}')