# Write a program that reads from the keyboard a positive integer and displays
# it in words(for example 25-twenty five,...)
# Dictionary for number words
num_words_1_to_19 = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

num_words_tens = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

def number_to_words(n):
    if n < 0:
        return "Please enter a positive integer."
    elif n < 20:
        return num_words_1_to_19[n]
    elif n < 100:
        tens = n // 10
        ones = n % 10
        if ones == 0:
            return num_words_tens[tens]
        else:
            return num_words_tens[tens] + "-" + num_words_1_to_19[ones]
    elif n < 1000:
        hundreds = n // 100
        remainder = n % 100
        if remainder == 0:
            return num_words_1_to_19[hundreds] + " hundred"
        else:
            return num_words_1_to_19[hundreds] + " hundred and " + number_to_words(remainder)
    elif n < 1000000:
        thousands = n // 1000
        remainder = n % 1000
        if remainder == 0:
            return number_to_words(thousands) + " thousand"
        else:
            return number_to_words(thousands) + " thousand, " + number_to_words(remainder)
    else:
        return "Number too large!"
try:
    number = int(input("Enter a positive integer: "))
    print(number_to_words(number))
except ValueError:
    print("Invalid input! Please enter a valid positive integer.")
