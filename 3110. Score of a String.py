def scoreOfString(s):
    score = 0
    for i in range(1, len(s)):
        cur = ord(s[i])
        prev = ord(s[i - 1])
        diff = abs(cur - prev)
        score = score + diff
    return score


def main():
    strings = "python"
    ret = scoreOfString(strings)
    print(ret)


if __name__ == "__main__":
    main()
