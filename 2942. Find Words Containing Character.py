def findWordsContaining(words, x):
    temp = []
    j = 0
    for i in words:
        if x in i:
            temp.append(j)
        j = j + 1
    return temp


def main():
    listofword = ["hello", "world"]
    char = "d"
    ret = findWordsContaining(listofword, char)
    print(ret)


if __name__ == "__main__":
    main()
