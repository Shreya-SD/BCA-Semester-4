# A list of numbers to work with
numbers = [40, 10, 30, 20, 50]
print("Starting list:")
print(numbers)

# 1. insert - Adds an item at a specific position (index)
# Let's add 15 at index 1
numbers.insert(1, 15)
print("After inserting 15 at index 1:")
print(numbers)

# 2. pop - Removes an item at a specific position (and returns it)
# Let's remove the last item
numbers.pop()
print("After popping the last item:")
print(numbers)

# 3. reverse - Flips the order of the list
numbers.reverse()
print("List after reversing:")
print(numbers)

# 4. sort - Puts numbers in order (smallest to largest)
numbers.sort()
print("List after sorting:")
print(numbers)

# 5. count - Counts how many times a value appears
# Let's add another 10 first to show how it works
numbers.append(10)
print("Updated list for counting:")
print(numbers)
print("How many times 10 appears:")
print(numbers.count(10))

# 6. index - Finds the position of the first occurrence of a value
print("The position (index) of number 30 is:")
print(numbers.index(30))

# 7. clear - Removes everything from the list
numbers.clear()
print("List after clear:")
print(numbers)
