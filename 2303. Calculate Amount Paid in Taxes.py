def calculateTax(brackets, income):
    tax = 0.00000
    upper0 = upper1 = 0
    n = len(brackets)

    for i in range(n):
        upper1 = brackets[i][0]
        if income >= upper1:
            tax = tax + (upper1 - upper0) * (brackets[i][1]) / 100
        else:
            tax = tax + (income - upper0) * (brackets[i][1]) / 100
            break
        upper0 = upper1
    return tax


def main():
    brac = [[1, 0], [4, 25], [5, 50]]
    income = 5
    ret = calculateTax(brac, income)
    print(ret)


if __name__ == "__main__":
    main()
