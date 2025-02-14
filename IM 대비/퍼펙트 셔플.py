T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = list(input().split())
    shuffled = [0]*N

    for idx,card in enumerate(arr):
        if idx < N/2:
            shuffled[idx*2] = card

        else:
            for idx2,card2 in enumerate(shuffled):
                if card2==0:
                    shuffled[idx2]=card
                    break


    print(f'#{tc}',*shuffled)