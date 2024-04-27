#9 Palindrome Number

def isPalindrome(x: int) -> bool:
    if(x<0):
        return 0
    if(x==0):
        return 1
    x_new=" "
    x_new=str(x)
    x_rev=x_new[::-1]
    if(x_new==x_rev):
        return 1
    return 0

def main():
    num=int(input("Enter the number"))
    ans=isPalindrome(num)
    if(ans==True):
        print("Palindrome Number")
    else: 
        print("Not a palindrome number")


if __name__=='__main__':
    main()
