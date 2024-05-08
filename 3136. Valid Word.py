def isValid(word):
    if len(word) >= 3:
        count_v = count_c = 0
        for i in word:
            if i.isalnum():
                if i in "aieouAEIOU":
                    count_v = count_v + 1
                elif i.isalpha():
                    count_c = count_v + 1
            else:
                return False
        if count_v >= 1 and count_c >= 1:
            return True
    return False


def main():
    words = "234Adas"
    ret = isValid(words)
    if ret:
        print("Word is valid")
    else:
        print("Invalid word")


if __name__ == "__main__":
    main()
