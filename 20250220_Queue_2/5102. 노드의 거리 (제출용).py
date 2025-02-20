T = int(input())

for tc in range(1,T+1):

    V,E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        i,j = map(int,input().split())
        arr[i].append(j)
        arr[j].append(i)
    S,G = map(int,input().split())

    visited = [0]*(V+1)
    que = []
    que.append(S)
    visited[S] = 1
    arrive = False

    while que:
        v = que.pop(0)
        for w in arr[v]:
            if w==G:
                arrive = True
                visited[w] = visited[v]
                break
            if visited[w]==0:
                que.append(w)
                visited[w]=visited[v]+1
        if arrive:
            break

    print(f'#{tc} {visited[G]}')