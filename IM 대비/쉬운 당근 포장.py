T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(input().split())

    carrot = {}

    for i in arr:
        if i in carrot:
            carrot[i] += 1
        else:
            carrot[i] = 1


    carrot_key = list(carrot.keys())
    L = len(carrot)

    if L < 3:
        result = -1
    else:
        # 이제 두 개의 포인트를 설정하여, 당근을 세 종류로 나눠야한다.
        # 그냥 L씩 돌린다?
        sml_carrots = 0
        mid_carrots = 0
        lar_carrots = 0
        point = []
        for i in range(L):
            for j in range(i+1,L):
                point.append([i,j])
        for idx in point:
            for i in idx:



    print(f'#{tc} ')