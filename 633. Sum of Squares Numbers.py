from collections import defaultdict


def judgeSquareSum(c):
    root = int(c ** (0.5))
    if root**2 == c:
        return True
    temp = defaultdict(int)
    for i in range(0, root + 1):
        temp[i**2] = 1
        if temp[c - i**2]:
            return True

    return False


def main():
    num = 10
    ret = judgeSquareSum(num)
    print(ret)


if __name__ == "__main__":
    main()
