T = int(input())

for tc in range(1, T+1):
    buses = int(input())
    busstoplist = [0]*5001
    for bus in range(buses):
        lineinfo = list(map(int,input().split()))
        for stop in range(lineinfo[0], lineinfo[1]+1):
            busstoplist[stop] += 1

    print(f'#{tc}', end=' ')

    stopnumber = int(input())

    for stop in range(stopnumber):
        print(f'{busstoplist[int(input())]}', end=' ')

    print()