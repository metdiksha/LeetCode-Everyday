def defangIPaddr(address):
    str1 = []
    address1 = address.split(".")
    for i in address1:
        str1.append(i)

    delimiter = "[.]"
    ret = delimiter.join(str1)
    return ret


def main():
    address = "1.1.1.1"
    ret = defangIPaddr(address)
    print(ret)


if __name__ == "__main__":
    main()
