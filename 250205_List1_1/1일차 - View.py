

for tc in range(1, 11):

    length = int(input())
    tower = list(map(int, input().split()))

    view = 0

    for i in range(2, length-2):
        minview = 255
        view1 = tower[i] - tower[i-2]
        view2 = tower[i] - tower[i-1]
        view3 = tower[i] - tower[i+1]
        view4 = tower[i] - tower[i+2]
        if view1 < minview:
            minview = view1
        if view2 < minview:
            minview = view2
        if view3 < minview:
            minview = view3
        if view4 < minview:
            minview = view4
        if minview > 0:
            view += minview

    print(f'#{tc} {view}')