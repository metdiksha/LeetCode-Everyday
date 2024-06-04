def reverse(x):
    rev = 0
    if x < 0:
        flag = -1
    else:
        flag = 1
    x = abs(x)
    while x > 0:
        rem = x % 10
        x = x // 10
        rev = rev * 10 + rem
    if (rev * flag <= (-(2**31))) or (rev * flag >= (2**31 - 1)):
        return 0
    return rev * flag


def main():
    num = -10499
    ret = reverse(num)
    print(ret)


if __name__ == "__main__":
    main()
