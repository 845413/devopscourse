def is_prime(num):
    # Check if num is less than 2 (prime numbers are greater than 1)
    if num <= 1:
        return False
    # Check divisibility from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # num is divisible by i, so it's not prime
    return True  # num is prime

# Input from user
number = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
