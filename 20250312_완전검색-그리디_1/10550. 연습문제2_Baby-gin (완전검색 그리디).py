import sys
sys.stdin = open('input.txt','r')


def is_babygin():
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
        return True
    else:
        return False


def f(i, N):
    global ans
    if i == N:
        if is_babygin():
            ans = 'Baby Gin'
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i + 1, N)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    a = list(map(int, input()))
    used = [0] * 6
    p = [0] * 6
    ans = 'Lose'
    f(0, 6)
    print(f'#{tc} {ans}')


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