def is_palindrome(s):
    i = 0
    e = len(s)-1
    while  i <= e :
        if s[i] == s[e]:
            i += 1
            e -= 1
        else:
            return False
    return True

print(is_palindrome('hello'))
print(is_palindrome('baab'))
