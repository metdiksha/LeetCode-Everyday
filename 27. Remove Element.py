def removeElement(nums, val) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


def main():
    nums = [1, 2, 3, 1]
    val = 1
    n = removeElement(nums, val)
    print("Number of elements left : ", n)


if __name__ == "__main__":
    main()
