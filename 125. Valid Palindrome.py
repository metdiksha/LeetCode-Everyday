def isPalindrome(s):
    lst = []
    for i in s:
        if i.isalnum():
            if i.isalpha():
                if i.isupper():
                    lst.append(i.lower())
                else:
                    lst.append(i)

            else:
                lst.append(i)
    rev = lst[::-1]
    if lst == rev:
        return True
    else:
        return False


def main():
    ret = isPalindrome("Hey 121 yeh")
    if ret == True:
        print("palindrome")
    else:
        print("not a palindrome")


if __name__ == "__main__":
    main()
