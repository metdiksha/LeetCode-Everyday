def intToRoman(num):
    string = []
    if num >= 1000:
        m_count = num // 1000
        num = num % 1000
        string.append("M" * m_count)
    if num >= 500:
        if num >= 900 and num <= 999:
            string.append("CM")
            num = num - 900
        else:
            d_count = num // 500
            num = num % 500
            string.append("D" * d_count)
    if num >= 100:
        if num >= 400 and num <= 499:
            string.append("CD")
            num = num - 400
        else:
            c_count = num // 100
            num = num % 100
            string.append("C" * c_count)
    if num >= 50:
        if num >= 90 and num <= 99:
            string.append("XC")
            num = num - 90
        else:
            l_count = num // 50
            num = num % 50
            string.append("L" * l_count)
    if num >= 10:
        if num >= 40 and num <= 49:
            string.append("XL")
            num = num - 40
        else:
            x_count = num // 10
            num = num % 10
            string.append("X" * x_count)
    if num >= 5:
        if num == 9:
            string.append("IX")
            num = num - 9
        else:
            v_count = num // 5
            num = num % 5
            string.append("V" * v_count)
    if num >= 1:
        if num == 4:
            string.append("IV")
            num = num - 4
        else:
            i_count = num // 1
            num = num % 1
            string.append("I" * i_count)

    return "".join(string)


def main():
    integer = 4589
    ret = intToRoman(integer)
    print("Roman is:", ret, "integer is: ", integer)


if __name__ == "__main__":
    main()
