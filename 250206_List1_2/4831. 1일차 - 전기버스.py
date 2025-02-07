T = int(input())

for tc in range(1, T+1):
    max_travel, arrival, num = map(int, input().split())

    chargable = list(map(int,input().split()))

    # 충전소 목록을 정렬하자
    for i in range(num-1, 0, -1):
        for j in range(i):
            if chargable[j] > chargable[j+1]:
                chargable[j], chargable[j+1] = chargable[j+1], chargable[j]

    bus = 0     # 버스의 현재 위치
    charge_count = 0    # 충전 횟수

    # print(f'버스위치: {bus}')

    while bus+max_travel < arrival:

        bus_before = bus

        for station in chargable:
            # print(f'버스위치: {bus}')
            # print(f'스테이션: {station}')
            if bus < station <= bus_before+max_travel:  # 충전 스테이션은 이 사이에 있어야 함
                bus = station                   # 최대한 먼 곳에서 충전을 하고 버스 위치 갱신
                # print(f'버스위치: {bus}')
        charge_count += 1                       # 충전 횟수 증가
        # print(charge_count, '****')

        if bus == bus_before:                   # 충전에 실패했다면
            charge_count = 0                    # 0으로 되돌리고 break
            break

    '''
    버스의 현재 위치에서 이동해서 도착하면? 해결
    도착 못하면? 충전이 필요함
    즉, 현재 위치 + 이동가능 거리 이전 가장 근접한 정류장에서 충전을 해야한다.
    현재 위치 + 이동 가능 거리 이전에 충전소가 없다면? 0을 프린트하고 넘어간다.
    '''

    print(f'#{tc} {charge_count}')





