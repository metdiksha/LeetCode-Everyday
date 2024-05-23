def sortSentence(s):

    temp = s.split()
    alist = [None] * (len(temp))

    for i in temp:
        n = len(i)
        pos = int(i[n - 1]) - 1
        hi = i[: n - 1]
        alist[pos] = hi

    st = " ".join(alist)
    return st


def main():
    s = "is2 sentence4 This1 a3"
    ret = sortSentence(s)
    print(ret)


if __name__ == "__main__":
    main()
