for _ in range(1,11):

    tc = int(input())
    arr = list(map(int,input().split()))

    finish = False

    while finish is False:
        for i in range(1,6):
            if arr[0]-i > 0:
                arr.append(arr.pop(0)-i)
            else:
                arr.append(0)
                arr.pop(0)
                finish = True
                break




    print(f'#{tc}',*arr)