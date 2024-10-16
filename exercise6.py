# Write a program that takes a string and displays it without the vowels(e,i,o,u,a)
def removeString(j):
    vowels = "aeiUoAEIOU"
    result = ""
    for char in j:
        if char not in vowels:
            result = result + char
    return result
a = str(input("enter the string\n"))
print(removeString(a)) 
