def decode(encoded, first):
    ret = []
    ret.append(first)
    prev = ret[0]
    for i in encoded:
        next = prev ^ i
        ret.append(next)
        prev = next
    return ret


def main():
    encoded = [6, 2, 7, 3]
    first = 4
    ret = decode(encoded, first)
    print(ret)


if __name__ == "__main__":
    main()
