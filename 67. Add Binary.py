def addBinary(a, b):

    def toDec(num):
        sum = 0
        n = len(num)
        for i in range(n):
            sum = sum + int(num[i]) * 2 ** (n - i - 1)

        return sum

    def toBin(num):
        if num == 0:
            return ["0"]
        temp = []
        while num > 0:
            rem = num % 2
            num = num // 2
            temp.append(str(rem))
        temp = temp[::-1]
        return temp

    val_a = toDec(a)
    val_b = toDec(b)

    val = val_a + val_b
    final_l = toBin(val)
    ret = "".join(final_l)
    return ret


def main():
    a = "11"
    b = "1001"
    ret = addBinary(a, b)
    print(ret)


if __name__ == "__main__":
    main()
