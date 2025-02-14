
def DNF(S,G,V):     # 출발, 도착, 개수
    visited = [0]*(V+1)
    stack = []

    while True:
        if S==G:
            return 1        # 도착 지점에 도착했다면 1을 반환하고 종료
        visited[S] = 1      # 출발 지점에 방문
        for g,n in enumerate(arr[S]):
            if n==1 and visited[g]==0:      # 인접한 and 방문안한 g 발견
                stack.append(S)             # 현재 정점 push
                S = g                       # g로 이동
                break
        else:                               # 더 이상 갈 곳이 없음
            if stack:                       # stack에 남은 값이 있다면
                S = stack.pop()             # 거기로 돌아간다 (이전 갈림길)
            else:
                return 0                  # 모두 탐색했는데 없었으니 0 반환


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    arr = [[0]*(V+1) for _ in range(V+1)]     # 인접행렬 생성
    for _ in range(E):
        i,j = map(int,input().split())
        arr[i][j] = 1                         # 일방통행이므로 ij만 추가한다

    S,G = map(int,input().split())

    print(f'#{tc} {DNF(S,G,V)}')