# A perfect number is a positive integer
# that is equal to the sum of its proper
# divisor.Write a python program that displays
#all perfect number between 1 and 1000000.
def is_perfect_number(n):
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                 divisor_sum += n // i
    return divisor_sum == n
perfect_numbers = []
for num in range(2, 1000001):
    if is_perfect_number(num):
        perfect_numbers.append(num)
print(f"Perfect numbers between 1 and 1,000,000: {perfect_numbers}")         
