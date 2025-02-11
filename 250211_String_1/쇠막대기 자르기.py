T = int(input())

for tc in range(1,T+1):
    '''
    ()  ((((  )  (() ((   ))  (   ))) (( ))
    '''
    arr = list(input())
    result = 0
    count = 0
    N = len(arr)

    for i in range(1, N):
        if arr[i-1]=='(' and arr[i]=='(':
            count += 1
        elif arr[i-1]=='(' and arr[i]==')':
            result += count
        elif arr[i-1]==')' and arr[i]==')':
            result += 1
            count -= 1

    print(f'#{tc} {result}')



    '''
    
    아래 코드도 맞음.. 그냥 너무 오래 걸려서 timeout이 뜰 뿐...
    
    laser = []
    sticks = []

    # 우선 레이저를 전부 파악하자. ()는 레이저다. 레이저가 발견되면 레이저를 0으로 지운다.
    for i in range(len(arr)-1):         # 인덱스 아웃을 방지하기 위해 마지막 하나 전까지만
        if arr[i]=='(' and arr[i+1]==')':
            arr[i], arr[i+1] = 0,0      # 레이저 발견! 지운다.
            laser.append(i)             # 레이저가 발견된 위치 기록

    # 이제 모든 쇠막대기를 찾을 것. 찾은 건 지우자. 다 지워질 때까지 찾자.
    count = 0
    while count < len(arr):
        count += 1
        for i in range(N):
            if arr[i]=='(':     # 쇠막대기는 (00...00) 형태로 존재한다.
                for k in range(1,N):
                    if 0<=i+k<N:    # 인덱스 안에서만 찾자
                        if arr[i+k]=='(':    # 이러면 쇠막대기가 아니다.
                            break
                        if arr[i+k]==')':   # 쇠막대기의 끝을 찾았다.
                            sticks.append([i,i+k])  # 막대기 시작, 끝 위치 기록
                            arr[i], arr[i+k] = 0,0  # 찾은 막대기 지우기
                            break           # 찾았으니 탈출하고 다른 막대기 찾으러 가자

    result = len(sticks)        # 자르기 전 막대기 개수

    #이제 각 레이저가 막대기를 몇 번씩 자르는지 살펴보자
    for beam in laser:
        for stick in sticks:
            if stick[0]<beam<stick[1]:
                result += 1
                
    '''
