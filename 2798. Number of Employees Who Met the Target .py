def numberOfEmployeesWhoMetTarget(hours, target):

    hours.sort(reverse=True)
    n = len(hours)

    if n == 0:
        return 0
    elif n == 1:
        if target < hours[0]:
            return 1
        else:
            return 0

    i = 0
    count = 0
    while i < n and hours[i] >= target:
        count = count + 1
        i = i + 1

    return count


def main():
    hrs = [4, 5, 7, 2, 3, 1, 8]
    target = 5
    ret = numberOfEmployeesWhoMetTarget(hrs, target)
    print(ret)


if __name__ == "__main__":
    main()
