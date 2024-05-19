def groupThePeople(groupSizes):
    n = len(groupSizes)
    adict = {}
    ret = []
    for i in range(n):
        if groupSizes[i] not in adict:
            adict[groupSizes[i]] = [i]
        else:
            adict[groupSizes[i]].append(i)
    for i in adict:
        while adict[i]:
            temp = adict[i][0:i]
            ret.append(temp)
            del adict[i][0:i]
    return ret


def main():
    gpsize = [3, 3, 3, 1, 1]
    ret = groupThePeople(gpsize)
    print(ret)


if __name__ == "__main__":
    main()
