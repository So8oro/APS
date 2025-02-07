T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = [0]
    chargers.extend(list(map(int, input().split())))
    num = 0
    bus = 0
    next_charger = 0  # 다음으로 충전할 충전기 위치
    while bus <= N:
        if bus + K >= N:
            bus = N
            break
        for i in range(next_charger, M + 2):
            if i == M + 1 or chargers[i] > bus + K:  # 충전기 위치가 갈 수 있는 거리보다 먼 경우
                num += 1
                break
            else:
                next_charger = i
        if bus == chargers[next_charger]:
            break
        bus = chargers[next_charger]
    if bus != N:
        num = 0

    print(f"#{tc} {num}")