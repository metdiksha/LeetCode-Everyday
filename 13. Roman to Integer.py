def romanToInt(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "C": 100, "L": 50, "D": 500, "M": 1000}
    n = len(s)
    sum = 0

    for i in range(n):
        if i == n - 1:
            sum = sum + roman[s[i]]

        if i != n - 1:
            if (roman[s[i + 1]]) > (roman[s[i]]):
                sum = sum - roman[s[i]]
            else:
                sum = sum + roman[s[i]]

    return sum


def main():
    s = "MCMXCIV"
    integer = romanToInt(s)
    print("Roman is:", s, "integr is: ", integer)


if __name__ == "__main__":
    main()
