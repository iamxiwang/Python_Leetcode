# 1. max value
# Write a function, max_value, that takes in list of numbers as an argument.    The function should return the largest number in the list.
# Solve this without using any built-in list methods.
# You can assume that the list is non-empty.
def max_value(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max

# 2 .is prime
# Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.
# A prime number is a number that is only divisible by two distinct numbers: 1 and itself.
# For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.
# You can assume that the input number is a positive integer.
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# is_prime(8) # -> False
# test_07:
# is_prime(25) # -> False
# test_08:
# is_prime(31) # -> True