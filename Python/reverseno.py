def reverse_math_method(n):
    n=int(input("enter number to be reversed:"))
    reversed_num = 0
    while n > 0:
        # Get the last digit (e.g., 123 % 10 = 3)
        last_digit = n % 10
        # Add it to the reversed number (shifting digits left)
        reversed_num = (reversed_num * 10) + last_digit
        # Remove the last digit from original (e.g., 123 // 10 = 12)
        n = n // 10
    return reversed_num

print(f"Original: {n} | Reversed: {reverse_math_method(n)}")
