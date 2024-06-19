def totalMoney(n):
    alist = [0, 0, 0, 0, 0, 0, 0]
    money = 0
    for i in range(n):
        j = i % 7
        if j == 0:
            alist[j] = alist[j] + 1
            money = alist[j] + money
            continue
        alist[j] = alist[j - 1] + 1
        money = money + alist[j]
    return money


def main():
    n = 100
    ret = totalMoney(n)
    print(ret)


if __name__ == "__main__":
    main()
