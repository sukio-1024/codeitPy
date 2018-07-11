def is_palindrome(word):
    check = False
    for i in range(0,int(len(word)/2)):
        if(word[i] == word[len(word) - i - 1]):
            check = True
        else:
            check = False
    if(check == True):
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))