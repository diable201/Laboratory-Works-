def hanoi(a, b, c, k):
    if k == 1:
        print(k, a, c)
    else:
        hanoi(a, c, b, k - 1)
        print(k, a, c)
        hanoi(b, a, c, k - 1)


def main():
    k = int(input())
    hanoi(1, 2, 3, k)


if __name__ == '__main__':
    main()
