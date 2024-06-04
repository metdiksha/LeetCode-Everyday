def myAtoi(s):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    num = str(num)
    read = []
    res = 0
    count = 0
    for i in s:
        if i.isalpha():
            break

        elif i == " ":
            if len(read) == 0:
                continue
            else:
                break
        elif i == "-":
            if len(read) == 0:
                read.append(i)
            else:
                break
        elif i == "+":
            if len(read) == 0:
                read.append(i)
            else:
                break
        elif i in num:
            read.append(i)
        else:
            break
    if read == []:
        return 0
    else:
        intersection_set = set(num).intersection(set(read))

        if len(intersection_set) == 0:
            return 0

    inte = "".join(read)
    if inte[0] == "-":
        integ = int(inte[1:]) * -1
        if integ < (-(2**31)):
            return -(2**31)
    elif inte[0] == "+":
        integ = int(inte[1:])
        if integ >= (2**31 - 1):
            return 2**31 - 1
    else:
        integ = int(inte)
        if integ >= 2**31 - 1:
            return 2**31 - 1

    return integ


def main():
    s = "-84*Hello world"
    ret = myAtoi(s)
    print(ret)


if __name__ == "__main__":
    main()
