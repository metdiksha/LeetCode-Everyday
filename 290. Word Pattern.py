def wordPattern(pattern, s):
    n_pattern = len(pattern)
    lst = s.split()
    n_lst = len(lst)
    if n_lst != n_pattern:
        return False
    dict_temp = {}
    flag = True
    for i in range(0, n_lst):
        if pattern[i] not in dict_temp:
            dict_temp[pattern[i]] = [lst[i]]
        else:
            dict_temp[pattern[i]].append(lst[i])
    for i in dict_temp:
        temp = dict_temp[i]
        n = len(temp)
        if n == 1:
            continue

        for j in range(n - 1):
            if temp[j] != temp[j + 1]:
                flag = False
    for j in pattern:
        for k in pattern:
            if j != k:
                if dict_temp[j] == dict_temp[k]:
                    flag = False

    return flag


def main():
    pattern = "aaa"
    s = "dog cat dog"
    ret = wordPattern(pattern, s)
    if ret:
        print("true")
    else:
        print("False")


if __name__ == "__main__":
    main()
