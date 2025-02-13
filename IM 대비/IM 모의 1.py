T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr에 들어있는 값을 중복 없이 저장할 세트
    arr_values = set()
    max_area = 0
    count = 0

    # 특정 값의 모든 위치를 기록할 리스트

    # 그냥 다 돌자
    for i in range(N):
        for j in range(N):
            arr_values.add(arr[i][j])

    arr_values = list(arr_values)

    # 밸류 하나씩 다 보자
    for value in arr_values:
        target = []     # 타겟값들의 위치 저장
        for i in range(N):
            for j in range(N):
                if arr[i][j] == value:
                    target.append([i,j])
        # 이제 target 에는 모든 현재 value의 위치가 기록되어 있다.
        # 가능한 모든 2개 조합을 골라내자.

        for target1 in target:
            for target2 in target:

                # 1을 더해야 같은 줄에 있는 부분배열의 넓이가 정상적으로 계산됨
                # 부호가 다르므로 우하단 - 좌상단으로 한번만 카운트
                area = (target1[0]-target2[0]+1)*(target1[1]-target2[1]+1)

                # 최대 넓이가 갱신되었다면? count를 1로 초기화한다.
                if area > max_area:
                    count = 1
                    max_area = area
                # 기존 최대 넓이와 같다면? 새로운 싸피부분배열을 찾았다.
                elif area == max_area:
                    count += 1


    print(f'#{tc} {count}')