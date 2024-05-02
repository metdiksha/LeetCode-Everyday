def isValid(s: str) -> bool:

    if len(s) % 2 == 1:
        return False
    stack = []
    flag = 1
    for i in s:
        if i not in "(){}[]":
            flag = 0
            break
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        else:
            if i == "}":
                if len(stack) != 0:
                    val = stack.pop()
                    if val == "{":
                        continue
                    else:
                        flag = 0
                        break
                else:
                    flag = 0
            elif i == "]":
                if len(stack) != 0:
                    val = stack.pop()
                    if val == "[":
                        continue
                    else:
                        flag = 0
                        break
                else:
                    flag = 0
            elif i == ")":
                if len(stack) != 0:
                    val = stack.pop()
                    if val == "(":
                        continue
                    else:
                        flag = 0
                        break
                else:
                    flag = 0
    if flag == 1 and len(stack) == 0:
        return True
    return False


def main():
    ret = isValid("<<")
    if ret == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
