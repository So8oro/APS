def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]=='2':
                return i,j
    print('wrong maze')
    return

def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)]
    que = []
    que.append([i,j])
    visited[i][j] = 1

    while que:
        vi,vj = que.pop(0)
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = vi+di,vj+dj
            if 0<=ni<N and 0<=nj<N:
                if maze[ni][nj]=='3':
                    return 1
                elif maze[ni][nj]!='1' and visited[ni][nj]==0:
                    que.append([ni,nj])
                    visited[ni][nj]=1

    return 0

for _ in range(1,11):
    tc = input()
    maze = [list(input()) for _ in range(16)]

    i,j = find_start(maze)
    result = bfs(i,j,16)

    print(f'#{tc} {result}')