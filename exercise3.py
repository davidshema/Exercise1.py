# Write a python program that does the following;
# 1. Generate 100 random integers between 1 and 50 and store them in a list.
# 2. Comput the mean,mode,starndard deviation,median of the numbers in the list.
import random
import statistics
random_numbers = [random.randint(1, 50) for _ in range(100)]
mean_value = statistics.mean(random_numbers)
mode_value = statistics.mode(random_numbers)
std_dev_value = statistics.stdev(random_numbers)
median_value = statistics.median(random_numbers)
print(f"List of random numbers: {random_numbers}")
print(f"Mean: {mean_value}")
print(f"Mode: {mode_value}")
print(f"Standard Deviation: {std_dev_value}")
