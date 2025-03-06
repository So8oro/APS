hex_to_dec = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}


def hex_bin(arr):
    bin_for = ""
    for x in arr[::-1]:
        four = ''
        dec = hex_to_dec[x]
        while dec > 0:
            remain = dec % 2
            four += str(remain)
            dec //= 2

        while len(four) < 4:
            four += '0'
        bin_for += four

    return bin_for[::-1]


def bin_to_dec(n):
    decimanl_number = 0
    pow = 0  # 지수
    for digit in reversed(n):
        if digit == '1':
            decimanl_number += 2 ** pow
            pow += 1
        else:
            pow += 1
    return (decimanl_number)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    hex = input()

    bin_result = hex_bin(hex)

    l = len(hex) * 4
    new_l = l - l % 7
    print(f"#{tc}", end=' ')
    for i in range(0, new_l, 7):
        print(bin_to_dec(bin_result[i:i + 7]), end=' ')
    print()