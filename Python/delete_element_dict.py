my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Original Dictionary:", my_dict)

# Delete an element using 'del'
del my_dict["age"]
print("Dictionary after deleting 'age':", my_dict)
# Delete an element using 'pop'
removed_value = my_dict.pop("city")
print("Removed value:", removed_value)
print("Dictionary after deleting 'city':", my_dict)
