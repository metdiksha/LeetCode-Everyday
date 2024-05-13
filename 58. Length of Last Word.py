def lengthOfLastWord(s):
    n = 0
    s = s[::-1]

    l = s.split(" ")

    for i in l:
        if i.isalpha():
            n = len(i)
            return n

    return n


def main():
    s = "Fly me to the moon   "
    ret = lengthOfLastWord(s)
    print(ret)


if __name__ == "__main__":
    main()
