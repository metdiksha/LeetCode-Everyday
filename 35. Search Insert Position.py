def searchInsert(nums, target):
    n = len(nums)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1

        else:
            return mid

    return start


def main():
    arr = [1, 3, 5, 6, 7]
    num = 4
    ret = searchInsert(arr, num)
    print(ret)


if __name__ == "__main__":
    main()
