import sys
sys.stdin = open('input.txt','r')

'''
자료 구조
 - 3개의 숫자 + 먹은 개수 저장
 - 리스트 보다는 변수로 저장해도 충분
 
알고리즘
 - B를 C보다 작을 때까지 하나씩 감소
  - [검증] 사탕의 개수가 많으면 시간 초과 가능성
   - 최대 3000개: 가능
 - 불가능한 케이스를 먼저 거르자 (하고나서 되는 케이스만 걸러도 됨)
  - B가 2보다 작은 경우, C가 3보다 작은 경우
'''

T = int(input())

for tc in range(1,T+1):
    A,B,C = map(int,input().split())

    if B<2 or C<3:
        print(f'#{tc} -1')
        continue

    cnt = 0
    if B>=C:
        cnt += B-C+1
        B -= cnt
    if A>=B:
        cnt += A-B+1

    print(f'#{tc} {cnt}')