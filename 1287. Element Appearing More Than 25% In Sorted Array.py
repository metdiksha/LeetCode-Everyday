def findSpecialInteger(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    Keymax = max(zip(count.values(), count.keys()))[1]

    return Keymax


def main():
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    ret = findSpecialInteger(arr)
    print(ret)


if __name__ == "__main__":
    main()
