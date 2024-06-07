def isAnagram(s, t):
    temp1 = list(s)
    temp2 = list(t)
    temp1.sort()
    temp2.sort()
    if temp1 == temp2:
        return True
    return False


def main():
    s = "this is me"
    t = "is this me"
    ret = isAnagram(s, t)
    if ret:
        print("It is a valid anagram")
    else:
        print("Not a valid anagram")


if __name__ == "__main__":
    main()
