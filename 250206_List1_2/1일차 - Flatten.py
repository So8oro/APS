for tc in range(1,11):

    dump = int(input())
    box_list = list(map(int,input().split()))

    for i in range(dump):

        high = 0
        low = 100
        idx_high = 0
        idx_low = 0

        for idx in range(100):
            if box_list[idx] > high:
                high = box_list[idx]
                idx_high = idx
            if box_list[idx] < low:
                low = box_list[idx]
                idx_low = idx

        box_list[idx_high] -= 1
        box_list[idx_low] += 1

    high = 0
    low = 100

    # 덤프 끝난 다음에 다시 체크해야 함 (덤프 후에도 최고 최저 높이가 변할수도 아닐수도)

    for idx in range(100):
        if box_list[idx] > high:
            high = box_list[idx]
        if box_list[idx] < low:
            low = box_list[idx]

    print(f'#{tc} {high-low}')