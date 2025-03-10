import sys
sys.stdin = open('input.txt','r')

'''
    1. 인풋을 받아와서 배열에 추가한다. start, end, order
    2. start, end 는 해당 학생의 이동 경로를 나타낸다.
    3. order 는 해당 학생이 몇번째에 이동할 수 있는지를 나타낸다.
     - 즉, order 가 1인 학생들은 모두 동시에 처음에 이동한다.
     - order 가 2인 학생들은 그 다음 모두 동시에 두번째로 이동한다.
     - 최대 order 가 결국 이동에 걸리는 총 시간
    4. 새로운 인풋을 받으면, 우선 order 가 1인 학생들을 전부 뽑아서 비교
     - 겹치는게 없으면, order 1로 배열에 추가
     - 겹치는게 있으면, order 2로 증가시키고 order가 2인 학생들을 뽑아서 비교
     - 마지막까지 겹치는게 있었다면, order 증가시키고 time 갱신하고 배열에 추가
'''

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    time = 1
    arr = []

    if N == 0:
        print(f'#{tc} 0')  # 모두 이미 자기 방이라면 시간은 0
        continue

    for _ in range(N):
        start, end = map(int, input().split())
        order = 1

        if start > end:  # 시작점 숫자가 더 작도록 조정
            start, end = end, start

        for t in range(1,time+1):   # 특정 타임에 이동할 수 있는지 볼까
            for s, e, o in arr:
                if o==t:            # 해당 타임만 보자

                    if (start+1)//2 > (e+1)//2 or (end+1)//2 < (s+1)//2: # 안 겹치는 경우. 홀수와 그보다 1 큰 짝수는 같은 복도를 공유함에 유의.
                        pass    # 안 겹쳤으니까 해당 시간대 이어서 탐색

                    else:
                        order += 1  # 겹쳤으면 다음 타임으로 넘어가자

                        break # 현재 오더 비교를 종료하고 다음 오더로 넘어감

            # 전부 안 겹쳤으면 해당 오더에 추가해야한다.
            # if order==t:
            else:
                break

        arr.append([start, end, order])
        if order == 1+time:
            time = order

    print(f'#{tc} {time}')