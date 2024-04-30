def palindrome(string):
    if string[::-1]==string:
        return True
    else:
        return False
s=input()
print(palindrome(s))