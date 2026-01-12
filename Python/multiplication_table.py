# A simple program to print multiplication tables
num = int(input("Enter the number for the table: "))
print(f"--- Table of {num} ---")
# The 'for' loop uses a colon and indentation instead of braces
for i in range(1, 11):
    result = num * i
    # Everything inside this indented block repeats 10 times
    print(f"{num} x {i} = {result}")
print("Table generation complete!")
