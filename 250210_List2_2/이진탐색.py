T = int(input())

for tc in range(1,T+1):

    P, Pa, Pb = map(int,input().split())
    Pca = 0
    Pcb = 0
    l=1
    r=P
    count_a = 0
    count_b = 0

    while Pca != Pa:
        count_a += 1
        Pca = int((l+r)/2)
        if Pca > Pa:
            r = Pca
        else:
            l = Pca

    l = 1
    r = P

    while Pcb != Pb:
        count_b += 1
        Pcb = int((l+r)/2)
        if Pcb > Pb:
            r = Pcb
        else:
            l = Pcb

    if count_a < count_b:
        winner = 'A'
    elif count_a == count_b:
        winner = 0
    else:
        winner = 'B'

    print(f'#{tc} {winner}')