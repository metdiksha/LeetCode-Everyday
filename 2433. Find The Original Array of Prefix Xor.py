def findArray(pref):
    prev = pref[0]
    alist = []
    if len(pref) == 0:
        return alist
    elif len(pref) == 1:
        return pref
    elif len(pref) == 2:
        alist.append(prev)
        next = prev ^ pref[1]
        alist.append(next)
        return alist
    alist.append(prev)
    for i in range(1, len(pref)):
        prev = pref[i - 1] ^ pref[i]
        alist.append(prev)
        print(prev)

    return alist


def main():
    pref = [5, 2, 0, 3, 1]
    ret = findArray(pref)
    print(ret)


if __name__ == "__main__":
    main()
