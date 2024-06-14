import math


def majorityElement(nums):
    temp = {}
    n = len(nums)
    for i in nums:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1
    ret = 0
    for i in temp:
        if temp[i] > (math.floor(n / 2)):
            ret = i
            break
    return ret


def main():
    arr = [2, 2, 1, 1, 1, 2, 2]
    ret = majorityElement(arr)
    print(ret)


if __name__ == "__main__":
    main()
