def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    allrot = []
    n = len(s)
    for i in range(n):
        temp = []
        temp.append(s[i + 1 : n])
        temp.append(s[: i + 1])
        allrot.append("".join(temp))
    if goal in allrot:
        return True
    return False


def main():
    s = "thisisme"
    goal = "ismethis"
    ret = rotateString(s, goal)
    print(ret)


if __name__ == "__main__":
    main()
