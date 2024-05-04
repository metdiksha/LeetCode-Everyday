def plusOne(digits):
    n = 0
    for i in digits:
        n = n * 10 + i

    inc = n + 1
    temp = []
    while inc != 0:
        val = inc % 10
        temp.append(val)
        inc = inc // 10

    temp = temp[::-1]

    return temp


def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ret = plusOne(li)
    print(ret)


if __name__ == "__main__":
    main()
