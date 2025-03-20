import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    # [시작, 끝, 거리]
    # 0에서 N 까지 가는 최소 거리
    # 0에서

    print(f'#{tc}')


    def dijkstra(s, N):
        U = [0] * (N + 1)  # U = {s}
        U[s] = 1  # U = [], U.append(0)
        D = [0] * (N + 1)  # D <- A[s]    #, 출발점에서 다른 정점으로 가는 비용
        # 저장용으로 미리 만들어두었다는 뜻이구나
        for i in range(N + 1):
            D[i] = adj_m[s][i]  # s 출발정점
            # 출발에서 i 로 가는 비용이 있다면, i에 저장한다. 즉 직행이 얼마인지. 없으면 우선 무한대
        # 출발점을 제외한 N개의 정점에 대한 비용 결정
        for _ in range(N):
            # 비용이 결정되지 않은 정점 중에 D[t]가 최소인 t
            min_v = INF
            t = 0
            for i in range(N + 1):
                if U[i] == 0 and min_v > D[i]:
                    min_v = D[i]
                    t = i
            U[t] = 1  # t는 최소비용 결정
            for j in range(N + 1):  # t에 인접한 j 찾기
                if 0 < adj_m[t][j] < INF:
                    D[j] = min(D[j], D[t] + adj_m[t][j])
        return D[N]


    INF = int(1e8)
    T = int(input())
    for tc in range(1, T + 1):
        N, E = map(int, input().split())  # 마지막 지점 번호 N과 도로의 개수 E
        # 인접행렬은 무한대로 초기화
        adj_m = [[INF] * (N + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            adj_m[i][i] = 0  # 자기 자신에 대한 비용 0
        for _ in range(E):
            s, e, w = map(int, input().split())
            adj_m[s][e] = w

        print(f'#{tc} {dijkstra(0, N)}')
