# A palindrome is a string that reads the same forward and backwards
# (for example madam,noon,.....)
# write a function that take a string as argument and return True if the string is a palindrome and False 
# otherwise
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("madam")) 
print(is_palindrome("noon"))  
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama")) 
