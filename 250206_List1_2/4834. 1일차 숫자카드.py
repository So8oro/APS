tc = int(input())
for tc in range(1, tc+1):
    N = int(input())
    arr = list(map(int,input()))

    card_list = [0]*10

    for i in range(N):
        card_list[arr[i]] += 1

    howmany = 0
    whichcard = 0

    for i in range(10):
        if card_list[i] >= howmany:
            howmany = card_list[i]
            whichcard = i

    print(f'#{tc} {whichcard} {howmany}')