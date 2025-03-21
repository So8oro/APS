import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,E = map(int,input().split())

    INF = 9990      # 끝지점이 1000, 가중치 최댓값이 10이므로 이론상 최댓값
    arr = [[INF]*(N+1) for _ in range(N+1)]     # 초기값은 최대로 설정

    for _ in range(E):
        s,e,w = map(int,input().split())
        arr[s][e] = w       # 직접 연결된 노드들에 값을 부여

    for i in range(N+1):
        arr[i][i] = 0       # 자기 자신과의 거리는 0

    U = [1]+[0]*N       # 최소거리가 확정된 노드는 1, 아닌 것은 0으로 표기. 시작점 자신은 확정되어 있음.
    D = [0]*(N+1)       # i번 노드까지의 현재 최소 거리를 저장

    # 일단 D에 직행 거리들을 저장하자
    for i in range(N+1):
        D[i] = arr[0][i]

    while U[N] != 1:        # U[N] == 1, 즉 최소거리임이 확정되면 종료하고 해당 값을 출력할 것이다.
        # 현재 제일 짧은 것을 찾아서 최소거리로 확정짓는다.
        min_v = INF
        t = 0
        for i in range(N+1):
            if U[i]==0 and min_v > D[i]:    # 0인거만 봐야 한다. 1인 것은 이미 이전에 최소로 확정된 것.
                min_v = D[i]
                t = i
        U[t] = 1

        # 이제 그 다음 값을 업데이트 해야한다. t에 인접한 점들을 업데이트 하자.
        for i in range(N+1):
            if arr[t][i] < INF:     # t에서 인접한 노드라면,
                D[i] = min(D[i], D[t]+arr[t][i])

    print(f'#{tc} {D[N]}')