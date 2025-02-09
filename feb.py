def fibonacci(n):
    # First two Fibonacci numbers
    fib_series = [0, 1]
    
    # Generate Fibonacci series up to n terms
    for i in range(2, n):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)
    
    return fib_series

# Input from the user
terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate and display the Fibonacci series
fib_sequence = fibonacci(terms)
print("Fibonacci series:")
print(fib_sequence)
