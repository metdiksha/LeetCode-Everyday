def frequencySort(s):
    temp_dict = {}
    for i in s:
        if i not in temp_dict:
            temp_dict[i] = 1
        else:
            temp_dict[i] = temp_dict[i] + 1

    temp = []
    while temp_dict:
        max_key = next(iter(temp_dict))
        for key in temp_dict:
            if temp_dict[key] > temp_dict[max_key]:
                max_key = key
        temp.append(temp_dict[max_key] * max_key)
        del temp_dict[max_key]
    return "".join(temp)


def main():
    s = "this is not me"
    ret = frequencySort(s)
    print(ret)


if __name__ == "__main__":
    main()
