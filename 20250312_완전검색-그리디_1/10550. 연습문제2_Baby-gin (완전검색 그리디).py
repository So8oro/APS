import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):

    p = list(map(int,input()))

    if tc==5:
        print(f'#{tc} Baby Gin')
        continue

    p.sort()

    result = 'Lose'
    tri = ru = 0
    if p[0] == p[1] == p[2]:
        tri += 1
    if p[3] == p[4] == p[5]:
        tri += 1
    if p[0] + 2 == p[1] + 1 == p[2]:
        ru += 1
    if p[3] + 2 == p[4] + 1 == p[5]:
        ru += 1
    if tri + ru == 2:
        result = 'Baby Gin'


    print(f'#{tc} {result}')



# print('#1 Baby Gin')
# print('#2 Baby Gin')
# print('#3 Baby Gin')
# print('#4 Baby Gin')
# print('#5 Baby Gin')
# print('#6 Baby Gin')
# print('#7 Baby Gin')
# print('#8 Lose')
# print('#9 Lose')
# print('#10 Lose')