def specialArray(nums):
    dict_count = {}
    max_ele = max(nums)
    for i in range(max_ele + 1):
        count = 0
        if i in dict_count:
            continue
        for j in nums:
            if j >= i:
                count = count + 1
        dict_count[i] = count
    for i in dict_count:
        if i == dict_count[i]:
            return i

    return -1


def main():
    nums = [3, 5]
    ret = specialArray(nums)
    print(ret)


if __name__ == "__main__":
    main()
