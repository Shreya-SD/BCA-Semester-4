def reverse_math_method():
    # 1. Get the number
    n = int(input("Enter number: "))
    original = n
    reversed_num = 0
    
    # 2. Do the math
    while n > 0:
        last_digit = n % 10
        reversed_num = (reversed_num * 10) + last_digit
        n = n // 10
    
    # 3. Give back both results
    return original, reversed_num

# 4. Run the function and save the results
orig, rev = reverse_math_method()

# 5. Print without the 'f'
print("Original:", orig, "| Reversed:", rev)
