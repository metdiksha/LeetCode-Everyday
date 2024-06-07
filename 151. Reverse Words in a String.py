def reverseWords(s):
    lst = s.split(" ")
    temp = []
    for i in lst:
        flag = 0
        word = []
        for j in i:
            if j.isalnum():
                word.append(j)
            else:
                flag = flag + 1
        if flag == len(i):
            continue
        temp.append("".join(word))
    temp = temp[::-1]
    return " ".join(temp)


def main():
    ret = reverseWords("this is 2 me3")
    print(ret)


if __name__ == "__main__":
    main()
