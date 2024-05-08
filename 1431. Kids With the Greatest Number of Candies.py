def kidsWithCandies(candies, extraCandies):
    max_ini = max(candies)
    ret = []
    for i in range(len(candies)):
        temp = candies[i] + extraCandies
        if temp >= max_ini:
            ret.append(True)
        else:
            ret.append(False)
    return ret


def main():

    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    ret = kidsWithCandies(candies, extraCandies)
    print(ret)


if __name__ == "__main__":
    main()
