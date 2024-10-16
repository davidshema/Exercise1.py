# Anagrams are strings containing the same set of letters(for example listen and enlist)
# write a function that taks two strings and return if they are anagram and false otherwise
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "enlist"))  
print(are_anagrams("hello", "world"))  
print(are_anagrams("astronomer", "moon starer")) 
