def reversePrefix(word, ch):

    if ch == "":
        return word
    ind = word.find(ch)
    print(ind)
    alist = list(map(str, word))
    temp = alist[: ind + 1]
    alist[0 : ind + 1] = temp[::-1]
    print(alist)
    delimiter = ""

    aword = delimiter.join(alist)

    return aword


def main():
    string = "hello"
    char = "e"
    ret = reversePrefix(string, char)
    print(ret)


if __name__ == "__main__":
    main()
