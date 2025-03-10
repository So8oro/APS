'''
전선 N개
 - 교차점 발생
 - 몇 개 발생하는지 count

교차점은 무슨 조건일 때 발생할까?
 - 새로운 선을 추가할 때
  - 기존 선과 비교
   1. 시작점이 높으며 도착점이 낮음
   2. 시작점이 낮으며, 도착점이 높음

리스트가 비어있어도 되나..?
'''

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = []
    cross = 0
    for _ in range(N):
        s,e = map(int,input().split())
        for S,E in arr:
            if (s<S and e>E) or (s>S and e<E):
                cross += 1
        arr.append([s,e])



    print(f'#{tc} {cross}')