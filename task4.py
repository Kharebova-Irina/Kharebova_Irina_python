import numpy as np
import sys


def main():
    if len(sys.argv) < 2:
        print("Введи числа через пробел")
        return

    try:
        a = list(map(int, sys.argv[1:]))
    except ValueError:
        print("Ошибка: все аргументы должны быть целыми числами")
        return

    if len(a) < 2:
        print("Ошибка: требуется минимум 2 числа")
        return

    cnt = 0
    min = a[0]

    for i in range(len(a)):
        while a[i] != min:
            if a[i] < min:
                a[i] += 1
                cnt += 1
            elif a[i] > min:
                a[i] -= 1
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
