def fractionToDecimal(numerator, denominator):

    if not numerator:
        return "0"
    rep = numerator / denominator
    print(rep)
    if rep in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return str(int(rep))

    temp = []

    str_rep = str(rep)
    lst = str_rep.split(".")
    if abs(numerator / denominator) > 1:
        temp.append(lst[0])
    else:
        if (numerator / denominator) > 0:
            temp.append("0")
        else:
            temp.append("-0")

    print(temp)

    if lst[1] == "0":
        return str(int(rep))
    else:
        numerator = abs(numerator)
        denominator = abs(denominator)
        remainder = numerator % denominator
        temp.append(".")

        remainder_positions = {}

        while remainder != 0:
            if remainder in remainder_positions:
                temp.insert(remainder_positions[remainder], "(")
                temp.append(")")
                break

            remainder_positions[remainder] = len(temp)
            remainder *= 10
            quotient = remainder // denominator
            temp.append(str(quotient))
            remainder %= denominator

    return "".join(temp)


def main():
    num = 9
    den = 566
    ret = fractionToDecimal(num, den)
    print(ret)


if __name__ == "__main__":
    main()
