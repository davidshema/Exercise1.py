# Write a python program that asks the user to input a positive and
# prints all prime numbers less than or equal to th input
# and only accepts positive integers as inputs.
def is_prime(num):
    if num < 1:
        return False
    for i in range (2, int(num/2) + 1):
        if num % i ==0:
            return False
    return True
def print_primes(n):
    for num in range(2,  n + 1):
        if is_prime(num):
            print(num)
a= int(input("Enter the number to show prime\n"))
print_primes(a)
