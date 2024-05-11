def convertTemperature(celsius):
    ans = []
    Kelvin = celsius + 273.15000
    ans.append(Kelvin)

    Fahrenheit = celsius * 1.80000 + 32.00000
    ans.append(Fahrenheit)

    return ans


def main():
    celsius = 36.50
    ret = convertTemperature(celsius)
    print(ret)


if __name__ == "__main__":
    main()
